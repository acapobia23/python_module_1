from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "mul":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(
    base_enchantment: Callable[..., str]
) -> dict[str, Callable[..., str]]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(base_enchantment, power=50,
                                     element="lightning")}


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[..., str]:
    @singledispatch
    def dispatch(arg) -> str:
        return f"Unknown spell type: {type(arg)}"

    @dispatch.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage dealt"

    @dispatch.register(str)
    def _(arg: str) -> str:
        return f"Enchantment spell: {arg} applied"

    @dispatch.register(list)
    def _(arg: list) -> str:
        return f"Multicast spells: {arg} cast"
    return dispatch


if __name__ == "__main__":
    print()
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "mul"))
    print("Max:", spell_reducer(spells, "max"))
    print()
    print("Testing memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print()
    disp = spell_dispatcher()
    print(disp(52))
    print()

    def enchant(power: int, element: str, target: str):
        return f"{target} has been fused with {element} and got +{power} power"
    ench = partial_enchanter(enchant)
    print(ench["fire_enchant"](target="sword"))
