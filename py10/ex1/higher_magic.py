from typing import Callable


def condition(power: int) -> bool:
    if power % 2 == 0:
        return True
    return False


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning shocks {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        new_power = power * multiplier
        res = base_spell(target, new_power)
        return res
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(power) is True:
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        seq = [spell(target, power) for spell in spells]
        return seq
    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    comb = spell_combiner(fireball, heal)
    res = comb("Drago", 42)
    print(f"Combined spell result: {res[0]}, {res[1]}")
    print()
    print("Testing power amplifier...")
    mega = power_amplifier(fireball, 3)
    print(mega("Dragon", 10))
    print()
    print("Testing conditional caster...")
    safe_fireball = conditional_caster(condition, fireball)
    print("True:", safe_fireball("Dragon", 10))
    print("False:", safe_fireball("Dragon", 11))
    print()
    print("Testing conditional caster...")
    sequence = spell_sequence([fireball, heal, lightning])
    seq_res = sequence("Drago", 58)
    for cast in seq_res:
        print(cast)
