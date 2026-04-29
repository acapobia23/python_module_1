from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def battle(opp: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    creatures = [(f.create_base(), s) for f, s in opp]
    len_ls = len(creatures)

    print("* Battle *")
    for i in range(len_ls):
        for j in range(i + 1, len_ls):
            crtr_one, fctr_one = creatures[i]
            crtr_two, fctr_two = creatures[j]
            print(crtr_one.describe())
            print(" vs.")
            print(crtr_two.describe())
            print(" now fight!")
            try:
                fctr_one.act(crtr_one)
                fctr_two.act(crtr_two)
            except Exception as e:
                print("Battle error, aborting tournament:", e)
                return


if __name__ == "__main__":
    factories = [
        FlameFactory(),
        AquaFactory(),
        HealingCreatureFactory(),
        TransformCreatureFactory(),
    ]

    strategies = [
        NormalStrategy(),
        AggressiveStrategy(),
        DefensiveStrategy(),
    ]

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    opps = [(factories[0], strategies[0]), (factories[2], strategies[2])]
    print("*** Tournament ***")
    print(f"{len(opps)} opponents involved\n")
    battle(opps)

    print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    opps = [(factories[0], strategies[1]), (factories[2], strategies[2])]
    print("*** Tournament ***")
    print(f"{len(opps)} opponents involved\n")
    battle(opps)

    print()

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opps = [(factories[1], strategies[0]),
            (factories[2], strategies[2]),
            (factories[3], strategies[1])
            ]
    print("*** Tournament ***")
    print(f"{len(opps)} opponents involved\n")
    battle(opps)


