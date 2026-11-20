#!/usr/bin/env python3
"""Validate the Serra Region authoring data without requiring the game toolchain."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "serra_region"
VALID_TYPES = {
    "NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "ROCK", "BUG",
    "GHOST", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC", "PSYCHIC",
    "ICE", "DRAGON", "DARK"
}

def load(name):
    with (DATA / name).open(encoding="utf-8") as f:
        return json.load(f)

def main():
    dex = load("species.json")
    league = load("gyms_and_league.json")
    species = dex["species"]
    errors = []

    if len(species) != 80 or dex["regionalDexCount"] != 80:
        errors.append("O catálogo deve conter exatamente 80 espécies.")
    ids = [p["regionalDex"] for p in species]
    names = [p["name"] for p in species]
    if sorted(ids) != list(range(1, 81)):
        errors.append("Os números da Pokédex regional devem ser contínuos de 1 a 80.")
    if len(names) != len(set(names)):
        errors.append("Há nomes de espécies duplicados.")
    if any(len(n) > 10 for n in names):
        errors.append("Há nomes maiores que 10 caracteres.")

    known = set(names)
    for p in species:
        if not p["types"] or len(p["types"]) > 2:
            errors.append(f'{p["name"]}: quantidade de tipos inválida.')
        if any(t not in VALID_TYPES for t in p["types"]):
            errors.append(f'{p["name"]}: tipo não suportado pela base Gen III.')
        stats = p["stats"]
        keys = ("hp", "attack", "defense", "speed", "spAttack", "spDefense")
        values = [stats[k] for k in keys]
        if any(v < 1 or v > 255 for v in values):
            errors.append(f'{p["name"]}: atributo-base fora do intervalo 1..255.')
        if sum(values) != stats["total"]:
            errors.append(f'{p["name"]}: total de atributos não confere.')
        evo = p.get("evolution")
        if evo and evo["to"] not in known:
            errors.append(f'{p["name"]}: evolução aponta para espécie inexistente.')

    gyms = league["gyms"]
    if len(gyms) != 8 or [g["order"] for g in gyms] != list(range(1, 9)):
        errors.append("A Serra deve ter exatamente oito ginásios em ordem.")
    for trainer in gyms + league["eliteFour"]:
        for mon, level in trainer["team"]:
            if mon not in known:
                errors.append(f'{trainer.get("leader", trainer.get("name"))}: espécie {mon} não existe.')
            if level < 1 or level > 100:
                errors.append(f'{trainer.get("leader", trainer.get("name"))}: nível inválido.')
    for mon, level in league["champion"]["team"]:
        if mon not in known:
            errors.append(f'Campeão: espécie {mon} não existe.')
        if level < 1 or level > 100:
            errors.append("Campeão: nível inválido.")

    if errors:
        print("\n".join("ERRO: " + e for e in errors))
        return 1
    print("OK: 80 espécies, evoluções, tipos e equipes da Liga validados.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
