def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda a: a["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":

    print("Testing artifact sorter...")

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Fire Staff", "power": 92, "type": "fire"},
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    print(f"{sorted_artifacts[0]['name']}"
          " ({sorted_artifacts[0]['power']} power) comes before "
          "{sorted_artifacts[1]['name']}"
          " ({sorted_artifacts[1]['power']} power)")

    print("Testing spell transformer...")

    spells = ["fireball", "heal", "shield"]

    transformed = spell_transformer(spells)

    print(" ".join(transformed))

    print("Testing power filter...")

    mages = [
        {"name": "Aeris", "power": 40, "element": "wind"},
        {"name": "Brann", "power": 75, "element": "fire"},
        {"name": "Cyril", "power": 55, "element": "ice"},
    ]

    filtered_mages = power_filter(mages, 60)

    print(", ".join(m["name"] for m in filtered_mages))

    print("Testing mage stats...")

    stats = mage_stats(mages)

    print(f"Max: {stats['max_power']}, Min: {stats['min_power']},"
          " Avg: {stats['avg_power']}")
