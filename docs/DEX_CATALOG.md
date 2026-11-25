# Serra & Calor — Regional Pokédex and Balance Audit

## Implementation snapshot

This document describes the data currently committed to `serra-region-foundation`. It distinguishes implemented data from remaining content work.

- 80 original Serra species, IDs 412–491.
- 26 three-stage evolution families (78 species) plus two single-stage legendary species.
- 21 additional species records for Serra/Calor regional and legendary forms, IDs 492–512.
- 12 original Calor species, IDs 513–524, arranged in four three-stage evolution families.
- 92 dedicated National Pokédex entries and English flavor-text records for the original Serra and Calor species (Dex 387–478).
- Regional forms reuse the National Pokédex number of their base species.
- All 113 custom species/form records have species-info, front/back sprite, front/back coordinate, palette, shiny-palette, and footprint entries.
- Regional cries currently reuse the cry associated with each species' aliased base sprite. These are varied placeholders, not newly recorded cries. All 113 custom species/form records now resolve to a matching existing cry.

The current graphics are table-level aliases to existing FireRed graphics. Original Serra/Calor sprite art, unique cries, maps, trainers, and story events are still separate content milestones.

## Serra — original species and evolution families

Evolution levels below are read from the committed evolution table. Types and base-stat totals are read from `species_info.h`.

| Evolution family | Type progression | Base-stat totals |
|---|---|---:|
| Snolet → Glacub → Bearice | Ice → Ice → Ice/Fighting | 300 → 402 → 510 |
| Pupsnow → Frostag → Aurorun | Ice/Normal → Ice/Normal → Ice/Psychic | 300 → 402 → 510 |
| Ironip → Ferritk → Cryotyr | Ice → Ice/Steel → Ice/Steel | 300 → 402 → 510 |
| Wraith → Chilume → Gloomice | Ghost → Ghost/Ice → Ghost/Ice | 300 → 402 → 510 |
| Penglit → Glacian → Emperor | Water → Water/Ice → Water/Ice | 300 → 402 → 510 |
| Dracub → Skalice → Nivadra | Dragon → Dragon/Ice → Dragon/Ice | 300 → 402 → 510 |
| Cindrift → Frostash → Pyrice | Fire → Fire/Ice → Fire/Ice | 300 → 402 → 510 |
| Mossnow → Fernice → Permoss | Grass → Grass/Ice → Grass/Ice | 300 → 402 → 510 |
| Tundrak → Nivalva → Borealis | Bug → Bug/Ice → Bug/Ice | 300 → 402 → 510 |
| Owlit → Snowl → Nocturn | Flying → Ice/Flying → Ice/Flying | 300 → 402 → 510 |
| Seallet → Glacial → Aurorseal | Water → Water/Ice → Water/Ice | 300 → 402 → 510 |
| Bergit → Glacer → Glacigol | Rock → Rock/Ice → Rock/Ice | 300 → 402 → 510 |
| Voltik → Stormelk → Thundra | Electric → Electric/Ice → Electric/Ice | 300 → 402 → 510 |
| Hushow → Wraithen → Umbrice | Ghost → Ghost/Ice → Ghost/Ice | 300 → 402 → 510 |
| Flurry → Rabblit → Avalynx | Normal → Normal/Ice → Normal/Ice | 300 → 402 → 510 |
| Mirrit → Mirroryx → Borealith | Psychic → Psychic/Ice → Psychic/Ice | 300 → 402 → 510 |
| Finlet → Glacfin → Rimeorca | Water → Water → Water/Ice | 300 → 402 → 510 |
| Iciclef → Spricleaf → Frostbloom | Grass → Grass/Ice → Grass/Ice | 300 → 402 → 510 |
| Moleice → Burrowst → Tundrill | Ground → Ground/Ice → Ground/Ice | 300 → 402 → 510 |
| Pugilit → Aegirush → Frostknit | Fighting → Fighting/Ice → Fighting/Ice | 300 → 402 → 510 |
| Poisonet → Venomelt → Cryoviper | Poison → Poison/Ice → Poison/Ice | 300 → 402 → 510 |
| Driflet → Snowmoth → Aurorwing | Bug/Flying → Bug/Flying → Ice/Flying | 300 → 402 → 510 |
| Pebblit → Snowstone → Tundragon | Rock → Rock/Ground → Rock/Dragon | 300 → 402 → 510 |
| Ashlet → Ashflake → Volcarime | Fire → Fire/Ground → Fire/Ground | 300 → 402 → 510 |
| Iceclam → Rimeshell → Leviacer | Water → Water/Steel → Water/Steel | 300 → 402 → 510 |
| Glacisau → Cryosaur → Glaciodon | Rock → Rock/Ice → Rock/Ice | 300 → 402 → 510 |

*Note: Evolution levels and type progressions are read from the committed data tables.*

### Legendary species

- **Boreas** — Ice/Flying, base-stat total 620.
- **Solstice** — Ice/Fire, base-stat total 635.
- **Serra Lugia** — Ice/Fairy, with Glaciate.
- **Serra Articuno** — Ice/Flying.
- **Serra Zapdos** — Ice/Electric.
- **Serra Moltres** — Fire/Ice.

The Galarian birds are also represented as separate forms: Articuno (Psychic/Flying), Zapdos (Fighting/Flying), and Moltres (Dark/Flying).

## Regional forms currently present

### Serra forms

- Vulpix / Ninetales: Ice; Ninetales gains Fairy.
- Sandshrew / Sandslash: Ice/Steel.
- Geodude / Graveler / Golem: Rock/Electric.
- Serra Articuno, Zapdos, Moltres, and Lugia.

### Calor forms

- Ho-Oh: Fairy/Fire.
- Cindrift / Frostash / Pyrice: Fire/Grass.
- Mossnow / Fernice / Permoss: Grass/Ground for the first two stages; the final Calor Permoss is Grass/Fairy.

### Calor — original species

| Evolution family | Type progression | Base-stat totals |
|---|---|---:|
| Solsprout → Solbloom → Solaris | Grass/Fire → Grass/Fire → Grass/Fairy | 300 → 405 → 515 |
| Cindrip → Magmolt → Pyroclast | Fire/Ground → Fire/Rock → Fire/Dragon | 300 → 410 → 520 |
| Oaslet → Mirajel → Mirageel | Water/Grass → Water/Psychic → Water/Fairy | 300 → 410 → 510 |
| Dustkit → Sandrake → Dunephant | Ground/Normal → Ground/Fire → Ground/Steel | 300 → 405 → 515 |

These twelve original species now have their own species IDs, evolutions, base stats, abilities, level-up learnsets, TM/HM and tutor compatibility, Pokédex pages, and entries in all species-indexed graphics tables. Their sprites and cries currently reuse FireRed assets for compactness; they are not original final artwork/audio.

**Calor is not yet a complete playable region.** It now has a real original twelve-species roster and the Ho-Oh/variant data, but its maps, encounter tables, story events, four gyms, League, and post-game travel are still unimplemented.

## Balance rules currently applied

- Three-stage Serra and Calor families use staged capture rates: 200 for first stage, 120 for middle stage, 45 for final stage.
- Their base experience yields are 64, 125, and 175 respectively.
- EV yields award 1, 2, or 3 points in the species' strongest base stat, based on evolution stage.
- Legendary forms/species use catch rate 3, base experience 220, and 3 EV points in their strongest stat.
- The 78 non-legendary Serra species and twelve Calor species use distinct stat allocations. Serra families use 300/402/510 BST targets; Calor families range from 300 at the first stage to 510–520 at the final stage. Different species emphasize bulk, physical attack, special attack, or speed.

These rules are an initial balance pass. Trainer teams, encounter rates, and in-game level curves still need playtesting before the values can be considered final.

## Technical integration completed

- The 80 Serra species have dedicated National Dex IDs 387–466; the twelve Calor species occupy 467–478.
- The National Dex count is 478 and includes the final Calor entry.
- National Dex species-to-entry mappings include all 92 original Serra and Calor species.
- All 21 additional regional/legendary forms map to their base species' National Dex entry to avoid duplicate dex pages.
- Alphabetical, type, height, and weight order lists include the 478-entry National Dex; forms remain mapped to their base pages.
- The expanded alphabetical list retains the legacy Old Unown values outside the active dex limit, matching the pre-existing layout.
- Each of the 92 original Serra/Calor species has a dedicated English Pokédex text record.
- All 113 custom species/forms resolve to the cry used by their aliased base sprite, rather than all sharing a single Swinub cry.
- TM/HM and tutor tables now extend through species ID 524, so newly added regional species do not index beyond those unsized arrays.

## Remaining quality gates

1. Replace sprite aliases with original front, back, icon, shiny-palette, and footprint art.
2. Record/compose distinct cries where appropriate; keep the alias fallback until custom audio is available.
3. Finish Calor's playable region: maps, encounters, story, four gyms, League, and travel unlock.
4. Verify every evolution, move learnset, TM/tutor compatibility, egg move, Pokédex entry, and battle ability.
5. Add Serra and Calor maps, encounters, trainer parties, gyms, story triggers, and travel connections.
6. Build both FireRed and LeafGreen targets and test the ROM in an emulator, including save data and all Pokédex ordering modes.
