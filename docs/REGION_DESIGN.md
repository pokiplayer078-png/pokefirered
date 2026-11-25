# Pokemon Serra & Calor — Project Roadmap

## Technical foundation
- Base: this repository, a Pokémon FireRed/LeafGreen decompilation (GBA).
- Working branch: `serra-region-foundation`.
- Target: a single GBA adventure with Serra as the main campaign and Calor as post-game content.
- Keep the original battle engine and data-driven systems wherever possible. Prefer reusing existing engine features and assets over adding heavyweight runtime systems.
- Build target remains a GBA ROM; do not silently convert this project into a browser game or a GBC ROM.

## Core premise
The player travels through Serra, a cold island/region whose climate is destabilizing. Galarian legendary birds are causing abnormal warming. The player investigates the environmental changes, finds Serra's regional legendary birds, and ultimately calls upon Serra Lugia to stop the crisis.

After the Serra League and main story, the player can travel to Calor, a warmer region with its own Pokémon, regional forms, gyms, and League challenge.

## Serra Region — main campaign
- Eight gyms.
- Regional Pokédex: 80 original Serra species already defined, plus regional forms and returning Pokémon.
- Serra Elite Four: Eira, Magnus, Nox, and Aster.
- Champion: Rowan.
- Legendary arc: Serra Articuno, Serra Zapdos, Serra Moltres, the Galarian birds as antagonists/causes of the crisis, and Serra Lugia.
- Regional forms should be varied: icy forms are part of the region but not every Pokémon should become Ice-type.
- Serra Lugia: Ice/Fairy.
- Signature ability, Glaciate: converts Normal-type moves used by its bearer into Ice-type moves. Implement as a battle-engine ability effect rather than a one-off scripted battle rule.

## Calor Region — post-game campaign
- Unlock after the main Serra story.
- Four gyms and a separate Champion/League challenge.
- Twelve original Calor Pokémon now defined across four evolution families, plus regional forms, with a warmer climate identity distinct from Serra.
- Calor Ho-Oh: Fairy/Fire.
- Keep the regional roster compact by sharing existing species data and graphics where appropriate.

## Design constraints
- Preserve FireRed's turn-based battle flow and GBA presentation.
- Avoid making every regional form Ice-type.
- Prioritize meaningful exploration, battles, side content, and progression over oversized maps or redundant encounters.
- Keep graphics, palettes, map layouts, and encounter tables reusable.
- Audit every species-indexed table whenever a species ID is added; keep the National Dex and battle data tables synchronized.

## Current implementation status (2026-11-25)

The working branch contains 80 original Serra species (IDs 412–491), twelve original Calor species (IDs 513–524), and 21 regional/legendary form records (IDs 492–512). The National Pokédex now has 478 entries, including dedicated pages for all 92 original Serra/Calor species. Species names, base stats, abilities, evolutions, level-up moves, machine/tutor compatibility, Pokédex records, graphics-table aliases, coordinates, footprints, and cry mappings have been connected.

Serra has its initial 26 three-stage families and two original legendary species. Calor has four original three-stage families: Solsprout, Cindrip, Oaslet, and Dustkit. The Calor roster is now more than a set of forms, but the region is not playable yet: maps, encounter tables, events, four gyms, its League, and travel unlock remain to be built.

The current sprites, party icons, palettes, footprints, and cries reuse FireRed assets as compact placeholders. Unique regional art and audio remain outstanding, and this branch has not yet been compiled into a ROM. See [DEX_CATALOG.md](DEX_CATALOG.md) for the data audit and the remaining quality gates.

## Implementation sequence
1. **Complete.** Lock the current roster: 80 original Serra species, 12 original Calor species, and 21 regional/legendary forms.
2. **Complete.** Audit species constants and all species-indexed tables; add a static regression checker.
3. **Partially complete.** Fairy typing and Glaciate have names, descriptions, battle damage and STAB conversion, and Serra Lugia is Ice/Fairy. AI matchup calculations now use the same Fairy and Glaciate rules; full battle tests remain.
4. **Partially complete.** Species data, evolutions, learnsets, TM/HM and tutor compatibility, Pokédex entries, sprite-table aliases, palettes, coordinates, footprints, and cry aliases are connected. Original art, icons where applicable, and distinct audio remain.
5. **Next major stage.** Build Serra maps, connections, warps, collision, events, trainers, encounters, and gym progression.
6. **Pending.** Implement the climate/legendary story flags and the Serra Lugia climax.
7. **Partially complete.** Calor has an original twelve-species roster and post-game design; its maps, events, four gyms, League, and travel unlock remain.
8. **In progress.** CI now validates the regional data and attempts FireRed/LeafGreen builds. Emulator, save compatibility, battle, and map playtesting remain.

## Current repository status

The active development branch is `serra-region-foundation` in [pokiplayer078-png/pokefirered](https://github.com/pokiplayer078-png/pokefirered/tree/serra-region-foundation). It contains:
- 80 original Serra species (IDs 412–491), 21 regional/legendary forms (492–512), and 12 original Calor species (513–524).
- 478 unique National Pokédex entries, with the forms sharing their base species' entries.
- 68 evolution links involving custom species, plus the full species data tables and compatibility mappings.
- A static checker at `tools/check_serra_calor_data.py`.
- A GitHub Actions workflow at `.github/workflows/serra-calor-build.yml` that checks the data and builds both GBA versions.

The graphics and audio aliases are compact placeholders using existing FireRed assets. Original regional art, maps, story events, trainer parties, gyms, the Calor League, and playable travel between the regions are not complete. The current CI's static data audit has passed; the GBA compilation is still running and no compiled ROM is being claimed here.
