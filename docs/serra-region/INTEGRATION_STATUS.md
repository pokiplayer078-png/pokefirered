# Serra Region — integration status

This document distinguishes source code already added from content that is still only designed.

## Integrated in source

| Area | Status |
|---|---|
| Internal species IDs | 101 entries, IDs 412–512; Egg moved to 513 |
| Species base data | Registered in `species_info.h` |
| Species names | Registered in `species_names.h` |
| Evolution table | 8 Serra/Calor regional evolution lines added |
| Level-up learnsets | 101 entries and pointers added; current sets are provisional |
| Front/back sprite tables | Valid fallback references for all 101 |
| Sprite coordinates | Entries for all 101 |
| Normal/shiny palettes | Valid fallback references for all 101 |
| Footprint table | Valid fallback references for all 101 |
| Party icons | Valid fallback references and palette indices for all 101 |
| Fairy type | Constant 18, type effectiveness overlay and battle grammar entry |
| Glaciate | Ability 78, description/name, damage type conversion, battle type calculation |
| Cry lookup | Custom IDs use a valid placeholder cry to avoid indexing beyond the existing cry list |
| Save progression | Reserved flag aliases for three Serra birds, Lugia called, Galar birds defeated and Calor bloomed |
| Starter/save variables | Story step and Calor state variable aliases |
| Starter area | Vila Flocos registered as a map, with sign, researcher NPC and Snolet Lv. 5 gift |
| First playable route | Vila Flocos now connects to a short-term reused route layout; low-level wild encounters include Snolet and early-game species |
| Route interaction | Researcher dialogue and route sign added; high-level route trainers removed from this beta slice |
| New-game access | Start point in Vila Flocos and a two-way map connection to the route are configured |
| New-game start | New games warp to Vila Flocos |
| Regional Lugia event | Vila Flocos NPC grants Lugia de Serra once, using the dedicated progression flag |
| Regional Ho-Oh revival | Vila Flocos NPC consumes exactly 10 Max Revives, revives Ho-Oh regional and grants it with guaranteed acquisition (no RNG capture roll) |

## Placeholder assets and incomplete systems

- All custom species currently reuse existing FireRed graphics. They are not their final artwork.
- Vila Flocos reuses the One Island layout and Sevii tileset; it is not yet a snowy town visually.
- The first route reuses the Kindle Road layout temporarily; its tiles, background, and map name still need replacement with original Serra assets.
- The new route currently uses low-level wild encounters (levels 4–8); Snolet uses placeholder FireRed graphics until original sprites are integrated.
- `WEATHER_SNOW` is marked unused in the base constants and must be made/verified in the overworld weather renderer.
- The full Galar bird sequence, legendary battle cinematics, and postgame world-state map variants are not connected yet. The first beta uses guaranteed scripted party acquisition for Lugia and revived Ho-Oh rather than a wild battle/capture animation.
- Calor's four gyms, champion and battles are planned data, not yet registered as actual map events/trainers.
- The National/Hoenn Pokédex conversion tables and Pokédex entry text/metadata are not yet extended for the new internal species.
- Fairy battle effectiveness is a first implementation. Fairy move coverage, type names, type icons, summary-screen presentation, AI effectiveness and other type-dependent systems still require integration.
- The current learnsets and stat spreads are initial drafts and require balancing.

## Validation completed

The branch was checked for:
- 101 unique species with sequential regional numbers;
- internal species IDs and Egg sentinel;
- species stats and names;
- all expected learnset pointers;
- graphics-table, coordinate, palette, footprint and icon entries;
- the 8 regional evolution links;
- Glaciate and Fairy battle hooks;
- 3 Serra birds, 3 Galar birds, 4 Calor gyms and a 6-member Calor champion team.

The data check returned no broken species/team references. This is source-level validation only, not a ROM build.

## Build verification

A draft pull request was opened so repository CI can assess the source changes:

- [Draft PR #1](https://github.com/pokiplayer078-png/pokefirered/pull/1)

The source now includes a minimal connected start-to-route loop and first-pass regional Lugia/Ho-Oh acquisition events, but no successful ROM build or mGBA playthrough has been confirmed yet. The GitHub Actions workflow is configured to build FireRed/LeafGreen and publish artifacts after pushes to `serra-region-foundation`. Do not treat this source snapshot as a tested ROM until that workflow succeeds and the ROM is checked in mGBA.
