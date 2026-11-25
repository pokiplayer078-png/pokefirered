# Serra & Calor — Regional Pokédex and Balance Audit

## Implementation snapshot

This document describes the data currently committed to `serra-region-foundation`. It distinguishes implemented data from remaining content work.

- 80 original Serra species, IDs 412–491.
- 26 three-stage evolution families (78 species) plus two single-stage legendary species.
- 21 additional species records for regional and legendary forms, IDs 492–512.
- 80 dedicated National Pokédex entries and flavor-text records for the original Serra species.
- Regional forms reuse the National Pokédex number of their base species.
- All 101 custom species/form records have front/back sprite table entries, palette entries, shiny palette entries, and species-info records.
- Regional cries currently reuse the cry associated with each species' aliased base sprite. These are varied placeholders, not newly recorded cries.

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
| Dracub → Skal ice → Nivadra | Dragon → Dragon/Ice → Dragon/Ice | 300 → 402 → 510 |
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

*Note: The species line names and levels above follow the code. “Skal ice” in older notes refers to the species constant `SKALICE`.*

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

**Calor is not yet a complete regional Pokédex.** At this snapshot, the code includes the Ho-Oh form and two Calor variants of existing Serra evolutionary families, but it does not yet have a separate roster of original Calor-only species, a Calor National Dex section, or a playable Calor map set. Those remain explicit follow-up work rather than being presented as completed features.

## Balance rules currently applied

- Three-stage Serra families use staged capture rates: 200 for first stage, 120 for middle stage, 45 for final stage.
- Their base experience yields are 64, 125, and 175 respectively.
- EV yields award 1, 2, or 3 points in the species' strongest base stat, based on evolution stage.
- Legendary forms/species use catch rate 3, base experience 220, and 3 EV points in their strongest stat.
- The 78 non-legendary Serra species now use distinct stat distributions instead of a repeated copy-paste spread. Their family-stage BST targets remain 300/402/510 to keep progression readable while different species emphasize bulk, physical attack, special attack, or speed.

These rules are an initial balance pass. Trainer teams, encounter rates, and in-game level curves still need playtesting before the values can be considered final.

## Technical integration completed

- The 80 Serra species have dedicated National Dex IDs 387–466.
- The National Dex count includes the last Serra entry.
- National Dex species-to-entry mappings include all original Serra species.
- All 21 additional forms map to their base species' National Dex entry to avoid duplicate dex pages.
- Alphabetical, type, height, and weight order lists include the expanded regional data.
- The expanded alphabetical list retains the legacy Old Unown values outside the active dex limit, matching the pre-existing layout.
- Each new species has a dedicated English Pokédex text record.
- Serra and Calor forms resolve to the cry used by their aliased base sprite, rather than all sharing a single Swinub cry.

## Remaining quality gates

1. Replace sprite aliases with original front, back, icon, shiny-palette, and footprint art.
2. Record/compose distinct cries where appropriate; keep the alias fallback until custom audio is available.
3. Design and implement Calor-only species and a separate Calor progression.
4. Verify every evolution, move learnset, TM compatibility, egg move, Pokédex entry, and battle ability.
5. Add Serra and Calor maps, encounters, trainer parties, gyms, story triggers, and travel connections.
6. Build both FireRed and LeafGreen targets and test the ROM in an emulator, including save data and all Pokédex ordering modes.
