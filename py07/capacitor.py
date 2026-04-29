import ex1
from ex0.creature import Creature

def healing_test(factory: ex1.HealingCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    show_healing(base)
    print(" evolved:")
    show_healing(evolved)

def show_healing(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def transform_test(factory: ex1.TransformCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    
    print("Testing Creature with transform capability")
    print(" base:")
    show_transform(base)
    print(" evolved:")
    show_transform(evolved)

def show_transform(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


if __name__ == "__main__":
    heal = ex1.HealingCreatureFactory()
    transform = ex1.TransformCreatureFactory()

    healing_test(heal)
    print()
    transform_test(transform)

