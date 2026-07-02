from typing import Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count = count + 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    base: int = initial_power

    def accumulator(add: int) -> int:
        nonlocal base
        base += add
        return base
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def factory(item_name: str) -> str:
        res = enchantment_type + " " + item_name
        return res
    return factory


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        return memory.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    count_a = mage_counter()
    count_b = mage_counter()

    print("Testing mage counter...")
    print("counter_a call 1:", count_a())
    print("counter_a call 2:", count_a())
    print("counter_b call 1:", count_b())
    print()

    count_a = spell_accumulator(100)
    count_b = spell_accumulator(100)
    print("Testing spell accumulator...")
    print("Base 100, add 20: ", count_a(20))
    print("Base 100, add 30: ", count_b(30))
    print()

    a = enchantment_factory("Flaming")
    b = enchantment_factory("Frozen")
    print("Testing enchantment factory...")
    print(a("Sword"))
    print(b("Shield"))
    print()
    print("Testing memory vault...")

    vault = memory_vault()

    print("Store 'secret'= 42")
    vault["store"]("secret", 42)

    print("Recall 'secret':", vault["recall"]("secret"))

    print("Recall 'unknown':", vault["recall"]("unknown"))
    print()


if __name__ == "__main__":
    main()
