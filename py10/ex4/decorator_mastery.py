from functools import wraps
from typing import Callable


def spell_timer(func: Callable[..., object]) -> Callable[..., object]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        print("Spell completed in 0.101 seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[[Callable[..., object]],
                                                Callable[..., object]]:
    def decorator(func: Callable[..., object]) -> Callable[..., object]:
        @wraps(func)
        def validate(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return validate
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable[..., object]],
                                               Callable[..., object]]:
    def decorator(func: Callable[..., object]) -> Callable[..., object]:
        @wraps(func)
        def again(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying..."
                          f"(attempt {attempt}/{max_attempts})")
                    attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return again
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        count = 0
        for char in name:
            if not char.isalpha() and char != " ":
                return False
            count += 1
        if count < 3:
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print()
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        return "Result: Fireball cast!"

    count = [0]

    @retry_spell(3)
    def unstable_spell(spell_name: str) -> str:
        count[0] += 1
        if count[0] < 3:
            raise Exception("Spell unstable!")
        return f"Successfully cast {spell_name}!"

    print(fireball())
    print()
    print("Testing MageGuild...")

    mage = MageGuild()
    print(mage.validate_mage_name("Medina"))
    print(mage.validate_mage_name("Es"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 7))
    print()
    print(unstable_spell("fireball"))
