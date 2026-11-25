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

The current sprites, palettes, footprints, and cries reuse FireRed assets as compact placeholders. Unique regional art and audio remain outstanding, and this branch has not yet been compiled into a ROM. See [DEX_CATALOG.md](DEX_CATALOG.md) for the data audit and the remaining quality gates.

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
