#!/usr/bin/env python3
"""Static consistency checks for the Serra & Calor regional Pokédex data."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    file_path = ROOT / path
    if not file_path.is_file():
        raise AssertionError(f"Missing required file: {path}")
    return file_path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def missing_entries(source: str, pattern: str, names: list[str]) -> list[str]:
    return [
        name for name in names
        if not re.search(pattern.replace("{NAME}", re.escape(name)), source)
    ]


def custom_species() -> list[tuple[int, str]]:
    source = read("include/constants/species.h")
    pairs = [
        (int(match.group(2)), match.group(1))
        for match in re.finditer(r"^#define SPECIES_([A-Z0-9_]+)\s+(\d+)$", source, re.M)
        if 412 <= int(match.group(2)) <= 524
    ]
    pairs.sort()
    require([species_id for species_id, _ in pairs] == list(range(412, 525)),
            "Custom species IDs must be continuous from 412 through 524.")
    require("#define SPECIES_EGG 525" in source, "SPECIES_EGG must follow the expanded roster.")
    require("#define NUM_SPECIES SPECIES_EGG" in source, "NUM_SPECIES must track SPECIES_EGG.")
    return pairs


def ordered_items(source: str, array_name: str) -> list[str]:
    match = re.search(
        rf"const u16 {re.escape(array_name)}\[\]\s*=\s*\{{(.*?)^\}};",
        source,
        re.M | re.S,
    )
    require(match is not None, f"Could not locate order array {array_name}.")
    return re.findall(r"^\s*([A-Z0-9_]+),\s*$", match.group(1), re.M)


def check() -> None:
    species_pairs = custom_species()
    all_names = [name for _, name in species_pairs]
    serra = [name for species_id, name in species_pairs if 412 <= species_id <= 491]
    forms = [name for species_id, name in species_pairs if 492 <= species_id <= 512]
    calor = [name for species_id, name in species_pairs if 513 <= species_id <= 524]
    require((len(serra), len(forms), len(calor)) == (80, 21, 12),
            "Expected 80 Serra species, 21 forms, and 12 original Calor species.")

    # Each custom species must exist in every core species-indexed table.
    checks = {
        "species names": ("src/data/text/species_names.h", r"\[SPECIES_{NAME}\]\s*="),
        "species info": ("src/data/pokemon/species_info.h", r"\[SPECIES_{NAME}\]\s*="),
        "level-up pointers": ("src/data/pokemon/level_up_learnset_pointers.h", r"\[SPECIES_{NAME}\]\s*="),
        "front sprites": ("src/data/pokemon_graphics/front_pic_table.h", r"SPECIES_SPRITE\({NAME}\s*,"),
        "back sprites": ("src/data/pokemon_graphics/back_pic_table.h", r"SPECIES_SPRITE\({NAME}\s*,"),
        "front coordinates": ("src/data/pokemon_graphics/front_pic_coordinates.h", r"\[SPECIES_{NAME}\]\s*="),
        "back coordinates": ("src/data/pokemon_graphics/back_pic_coordinates.h", r"\[SPECIES_{NAME}\]\s*="),
        "normal palettes": ("src/data/pokemon_graphics/palette_table.h", r"SPECIES_PAL\({NAME}\s*,"),
        "shiny palettes": ("src/data/pokemon_graphics/shiny_palette_table.h", r"SPECIES_SHINY_PAL\({NAME}\s*,"),
        "footprints": ("src/data/pokemon_graphics/footprint_table.h", r"\[SPECIES_{NAME}\]\s*="),
        "TM/HM compatibility": ("src/data/pokemon/tmhm_learnsets.h", r"\[SPECIES_{NAME}\]\s*="),
        "move tutor compatibility": ("src/data/pokemon/tutor_learnsets.h", r"\[SPECIES_{NAME}\]\s*="),
    }
    for label, (path, pattern) in checks.items():
        absent = missing_entries(read(path), pattern, all_names)
        require(not absent, f"{label} missing for: {', '.join(absent)}")

    learnsets = read("src/data/pokemon/level_up_learnsets.h")
    learnset_pointers = read("src/data/pokemon/level_up_learnset_pointers.h")
    species_names = read("src/data/text/species_names.h")
    for name in all_names:
        symbol = re.sub(r"(^|_)([a-z])", lambda m: m.group(2).upper(), name.lower())
        require(f"s{symbol}LevelUpLearnset[]" in learnsets,
                f"Missing level-up learnset for {name}.")
        require(f"[SPECIES_{name}]" in learnset_pointers,
                f"Missing learnset pointer for {name}.")
        require(f"[SPECIES_{name}]" in species_names,
                f"Missing display name for {name}.")

    # Evolution chains must stay inside the regional roster and be complete.
    evolution_data = read("src/data/pokemon/evolution.h")
    evolution_edges = re.findall(
        r"^\s*\[SPECIES_([A-Z0-9_]+)\]\s*=\s*\{\{EVO_LEVEL,\s*(\d+),\s*SPECIES_([A-Z0-9_]+)\}\}",
        evolution_data,
        re.M,
    )
    regional_edges = [(source, target) for source, _, target in evolution_edges if source in set(all_names)]
    require(len(regional_edges) == 68, f"Expected 68 regional evolution links; found {len(regional_edges)}.")
    require(len({source for source, _ in regional_edges}) == 68,
            "Regional evolution table has duplicate source species.")
    require(all(source in set(all_names) and target in set(all_names) for source, target in regional_edges),
            "Regional evolution link points outside the custom roster.")

    # Validate stat blocks, abilities, and EV totals.
    info = read("src/data/pokemon/species_info.h")
    for name in all_names:
        match = re.search(
            rf"\[SPECIES_{re.escape(name)}\]\s*=\s*\{{(.*?)^\s*\}},",
            info,
            re.M | re.S,
        )
        require(match is not None, f"Missing species-info block for {name}.")
        block = match.group(1)
        ability_match = re.search(r"\.abilities\s*=\s*\{([^}]+)\}", block)
        require(ability_match is not None and "ABILITY_NONE, ABILITY_NONE" not in ability_match.group(1),
                f"{name} has no functional ability.")
        stat_keys = ("HP", "Attack", "Defense", "Speed", "SpAttack", "SpDefense")
        stats = [
            int(re.search(rf"\.base{key}\s*=\s*(\d+)", block).group(1))
            for key in stat_keys
        ]
        require(all(1 <= stat <= 255 for stat in stats), f"Invalid base stat value for {name}.")
        evs = [
            int(re.search(rf"\.evYield_{key}\s*=\s*(\d+)", block).group(1))
            for key in stat_keys
        ]
        require(sum(evs) in (1, 2, 3), f"Invalid EV yield total for {name}: {sum(evs)}.")

    # Glaciate must be a named ability and be implemented in both battle damage and STAB/type checks.
    ability_constants = read("include/constants/abilities.h")
    ability_text = read("src/data/text/abilities.h")
    battle_scripts = read("src/battle_script_commands.c")
    pokemon_damage = read("src/pokemon.c")
    require("#define ABILITY_GLACIATE 78" in ability_constants,
            "Glaciate ability constant is missing or has moved.")
    require("[ABILITY_GLACIATE] = _(" in ability_text
            and "sGlaciateDescription" in ability_text,
            "Glaciate ability name or description is missing.")
    require("ABILITY_GLACIATE && moveType == TYPE_NORMAL" in battle_scripts,
            "Glaciate is not applied in the battle type/STAB script.")
    require("attacker->ability == ABILITY_GLACIATE && type == TYPE_NORMAL" in pokemon_damage,
            "Glaciate is not applied in the base damage calculation.")
    require("[SPECIES_LUGIA_S]" in info
            and ".types = {TYPE_ICE, TYPE_FAIRY}" in re.search(
                r"\[SPECIES_LUGIA_S\]\s*=\s*\{(.*?)^\s*\},", info, re.M | re.S
            ).group(1)
            and ".abilities = {ABILITY_GLACIATE, ABILITY_NONE}" in re.search(
                r"\[SPECIES_LUGIA_S\]\s*=\s*\{(.*?)^\s*\},", info, re.M | re.S
            ).group(1),
            "Serra Lugia must be Ice/Fairy and carry Glaciate.")

    # AI type calculations must mirror Fairy matchups and Glaciate conversion.
    battle_script_commands = read("src/battle_script_commands.c")
    battle_ai_switch_items = read("src/battle_ai_switch_items.c")
    battle_script_header = read("include/battle_script_commands.h")
    require("ApplyFairyTypeEffectiveness(move, moveType" in battle_script_commands,
            "Fairy type effectiveness overlay is missing from the shared type calculator.")
    require("attackerAbility == ABILITY_GLACIATE && moveType == TYPE_NORMAL" in battle_script_commands,
            "AI type calculations do not account for Glaciate.")
    require("u8 AI_TypeCalc(u16 move, u16 targetSpecies, u8 targetAbility, u8 attackerAbility)" in battle_script_commands
            and "u8 AI_TypeCalc(u16 move, u16 targetSpecies, u8 targetAbility, u8 attackerAbility);" in battle_script_header,
            "AI_TypeCalc must receive the attacking ability for Glaciate.")
    require("AI_TypeCalc(move, gBattleMons[opposingBattler].species, gBattleMons[opposingBattler].ability, attackerAbility)" in battle_ai_switch_items,
            "Party-switch AI does not pass its candidate's ability into AI_TypeCalc.")
    ai_calls = re.findall(r"AI_TypeCalc\(([^;]+)\);", battle_ai_switch_items)
    require(len(ai_calls) == 6 and all(len(call.split(",")) == 4 for call in ai_calls),
            "Every AI_TypeCalc call must supply the attacking ability.")

    # The 92 original species have independent Pokédex pages. The 21 forms share base entries.
    entries = read("src/data/pokemon/pokedex_entries.h")
    dex_records = re.findall(r"^\s*\[NATIONAL_DEX_([A-Z0-9_]+)\]\s*=", entries, re.M)
    dex_records = [name for name in dex_records if name != "NONE"]
    require(len(dex_records) == 478 and len(set(dex_records)) == 478,
            "Expected 478 unique non-empty National Pokédex records.")
    for name in serra + calor:
        require(re.search(rf"\[NATIONAL_DEX_{name}\]\s*=", entries),
                f"Missing individual Pokédex entry for {name}.")
    for name in forms:
        require(not re.search(rf"\[NATIONAL_DEX_{name}\]\s*=", entries),
                f"Regional form {name} should share its base species' Pokédex entry.")

    category_labels = re.findall(r'\.categoryName\s*=\s*_\("([^"]+)"\)', entries)
    require(category_labels and max(map(len, category_labels)) <= 11,
            "Pokédex category labels must fit the 12-byte categoryName field.")

    # Validate all four ordering arrays and prevent duplicate entries.
    orders = read("src/data/pokemon/pokedex_orders.h")
    expected_counts = {"Alphabetical": 503, "Type": 502, "Weight": 478, "Height": 478}
    for name, expected in expected_counts.items():
        values = ordered_items(orders, f"gPokedexOrder_{name}")
        require(len(values) == expected, f"{name} order has {len(values)} entries; expected {expected}.")
        require(len(values) == len(set(values)), f"{name} order contains duplicate entries.")

    pokedex_constants = read("include/constants/pokedex.h")
    require("#define NATIONAL_DEX_COUNT  NATIONAL_DEX_DUNEPHANT" in pokedex_constants,
            "National Dex count does not end at Dunephant.")
    require("POKEDEX_ORDER_ALPHABETICAL_COUNT" in pokedex_constants
            and "POKEDEX_ORDER_TYPE_COUNT" in pokedex_constants,
            "Missing explicit ordered-list length constants.")
    pokedex_screen = read("src/pokedex_screen.c")
    require("i < POKEDEX_ORDER_ALPHABETICAL_COUNT" in pokedex_screen
            and "i < POKEDEX_ORDER_TYPE_COUNT" in pokedex_screen,
            "Pokédex ordered-list loops are not bounded by their actual array sizes.")

    # Party icons and their palette indices must be populated for every custom species/form.
    icon_source = read("src/pokemon_icon.c")
    icon_table = re.search(
        r"const u8 \*const gMonIconTable\[\]\s*=\s*\{(.*?)^\};",
        icon_source,
        re.M | re.S,
    )
    icon_palette_table = re.search(
        r"const u8 gMonIconPaletteIndices\[\]\s*=\s*\{(.*?)^\};",
        icon_source,
        re.M | re.S,
    )
    require(icon_table is not None and icon_palette_table is not None,
            "Could not find the party icon or icon palette tables.")
    for name in all_names:
        require(re.search(rf"\[SPECIES_{re.escape(name)}\]\s*=\s*gMonIcon_", icon_table.group(1)),
                f"Missing party icon for {name}.")
        require(re.search(rf"\[SPECIES_{re.escape(name)}\]\s*=\s*[0-2],", icon_palette_table.group(1)),
                f"Missing or invalid party icon palette index for {name}.")

    # Species-indexed National Dex and cry maps must span the complete expanded range.
    pokemon_source = read("src/pokemon.c")
    dex_map_match = re.search(
        r"static const u16 sSpeciesToNationalPokedexNum\[NUM_SPECIES - 1\]\s*=\s*\{(.*?)^\};",
        pokemon_source,
        re.M | re.S,
    )
    require(dex_map_match is not None, "Could not find the species-to-National-Dex map.")
    require(len(re.findall(r"SPECIES_TO_NATIONAL\(", dex_map_match.group(1))) == 524,
            "Species-to-National-Dex map must cover all 524 species.")

    species_constants = {
        int(match.group(2)): match.group(1)
        for match in re.finditer(r"^#define SPECIES_([A-Z0-9_]+)\s+(\d+)$", read("include/constants/species.h"), re.M)
    }
    mapped_species = re.findall(r"SPECIES_TO_NATIONAL\(([A-Z0-9_]+)\)", dex_map_match.group(1))
    regional_form_bases = {
        492: "ARTICUNO", 493: "ZAPDOS", 494: "MOLTRES",
        495: "ARTICUNO", 496: "ZAPDOS", 497: "MOLTRES",
        498: "LUGIA", 499: "HO_OH", 500: "VULPIX", 501: "NINETALES",
        502: "SANDSHREW", 503: "SANDSLASH", 504: "GEODUDE",
        505: "GRAVELER", 506: "GOLEM", 507: "CINDRIFT",
        508: "FROSTASH", 509: "PYRICE", 510: "MOSSNOW",
        511: "FERNICE", 512: "PERMOSS",
    }
    expected_regional_map = [
        regional_form_bases[species_id] if species_id in regional_form_bases
        else species_constants[species_id]
        for species_id in range(412, 525)
    ]
    require(mapped_species[411:524] == expected_regional_map,
            "Regional National Dex mappings are not aligned to their species IDs.")


    cry_match = re.search(
        r"static const u16 sSerraCalorSpeciesToCryId\[\]\s*=\s*\{(.*?)^\};",
        pokemon_source,
        re.M | re.S,
    )
    require(cry_match is not None, "Could not find regional cry map.")
    require(len(re.findall(r"\[SPECIES_", cry_match.group(1))) == 113,
            "Regional cry map must cover all 113 custom species/forms.")
    require("species <= SPECIES_DUNEPHANT - 1" in pokemon_source,
            "Regional cry lookup range does not include Dunephant.")

    # Confirm the National Dex text includes both regions' independent entries.
    serra_text = read("src/data/pokemon/pokedex_text_serra.h")
    calor_text = read("src/data/pokemon/pokedex_text_calor.h")
    require(len(re.findall(r"const u8 g\w+PokedexText\[\]", serra_text)) == 80,
            "Expected 80 dedicated Serra Pokédex text records.")
    require(len(re.findall(r"const u8 g\w+PokedexText\[\]", calor_text)) == 12,
            "Expected 12 dedicated Calor Pokédex text records.")

    print("Serra & Calor regional data audit: PASS")
    print("80 Serra species | 21 regional/legendary forms | 12 Calor species")
    print("478 National Dex entries | 113 species/form data records verified")
    print("Species, learnsets, compatibility, graphics tables, Pokédex and ordering checks passed.")


if __name__ == "__main__":
    try:
        check()
    except (AssertionError, AttributeError, OSError) as error:
        print(f"Serra & Calor regional data audit: FAIL: {error}", file=sys.stderr)
        sys.exit(1)
