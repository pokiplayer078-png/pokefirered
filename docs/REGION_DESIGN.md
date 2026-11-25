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
- Regional Pokédex target: approximately 80 original Serra species, plus regional forms and returning Pokémon.
- Serra Elite Four: Eira, Magnus, Nox, and Aster.
- Champion: Rowan.
- Legendary arc: Serra Articuno, Serra Zapdos, Serra Moltres, the Galarian birds as antagonists/causes of the crisis, and Serra Lugia.
- Regional forms should be varied: icy forms are part of the region but not every Pokémon should become Ice-type.
- Serra Lugia: Ice/Fairy.
- Signature ability, Glaciate: converts Normal-type moves used by its bearer into Ice-type moves. Implement as a battle-engine ability effect rather than a one-off scripted battle rule.

## Calor Region — post-game campaign
- Unlock after the main Serra story.
- Four gyms and a separate Champion/League challenge.
- New Calor Pokémon and regional forms, with a warmer climate identity distinct from Serra.
- Calor Ho-Oh: Fairy/Fire.
- Keep the regional roster compact by sharing existing species data and graphics where appropriate.

## Design constraints
- Preserve FireRed's turn-based battle flow and GBA presentation.
- Avoid making every regional form Ice-type.
- Prioritize meaningful exploration, battles, side content, and progression over oversized maps or redundant encounters.
- Keep graphics, palettes, map layouts, and encounter tables reusable.
- Avoid allocating new species IDs until the complete roster and all dependent tables are audited together.

## Current implementation status (2026-11-25)

The working branch now contains 80 original Serra species (IDs 412–491), 21 additional form records (IDs 492–512), complete National Pokédex records for the 80 original species, species-to-dex mappings, and updated alphabetical/type/height/weight ordering. The custom roster also has distinct stage-based catch rates, experience yields, EV yields, varied stat profiles, and cry aliases matched to the base sprite used by each entry.

Calor is still a planned post-game region rather than a complete playable region. Current Calor data consists of the Ho-Oh form and Calor variants for the Cindrift and Mossnow lines. Original Calor-only species, maps, encounter tables, gyms, and story events have not yet been implemented. The current sprite table entries reuse existing FireRed graphics; original regional sprite art remains outstanding.

See [DEX_CATALOG.md](DEX_CATALOG.md) for the audited species list, typings, balance rules, and remaining quality gates.

## Implementation sequence
1. Lock the complete Serra and Calor species roster, forms, types, abilities, evolutions, and dex numbering.
2. Audit the current decomp's species constants and all species-indexed tables before extending them.
3. Implement Fairy typing and Glaciate with tests for move conversion, STAB, effectiveness, and AI behavior.
4. Add species data in one consistent pass: base stats, learnsets, evolutions, cries, icons, front/back sprites, palettes, dex entries, and footprints.
5. Build Serra maps, connections, warps, collision, events, trainers, encounters, and gym progression.
6. Implement the climate/legendary story flags and the Serra Lugia climax.
7. Add Calor as post-game, reusing engine systems and adding its four-gym challenge.
8. Compile and test the ROM regularly; validate map collision/warps, party and battle edge cases, and save compatibility.

## Current repository status
The branch `serra-region-foundation` is present. The FireRed decompilation remains the technical base. This document records the agreed design and implementation order; it does not claim that the region maps, species, sprites, or a playable ROM have already been implemented.
