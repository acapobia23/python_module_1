from ex0 import CreatureFactory
import ex0

def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())

def test_battle(f_water: CreatureFactory, f_fire: CreatureFactory) -> None:
    fire = f_fire.create_base()
    water = f_water.create_base()

    print("Testing battle")
    print(fire.describe())
    print(" vs.")
    print(water.describe())
    print(" fight!")
    print(fire.attack())
    print(water.attack())

if __name__ == "__main__":
    flame = ex0.FlameFactory()
    aqua = ex0.AquaFactory()
    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    test_battle(aqua, flame)
