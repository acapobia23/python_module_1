def input_temperature(temp_str :str) -> int:
    num = int(temp_str)
    if num > 40 or num < 0:
        raise ValueError
    return num

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
      print(f"Temperature is now {input_temperature("25")}°C")
    except ValueError as e:
        print(e)
    print()
    print("Input data is 'abc'")
    try:
      input_temperature("abc")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print()
    print("Input data is '100'")
    try:
      input_temperature("100")
    except ValueError as e:
        print("Caught input_temperature error: 100°C is too hot for plants (max 40°C)")
    print()
    print("Input data is '-50'")
    try:
      input_temperature("-50")
    except ValueError as e:
        print("Caught input_temperature error: -50°C is too cold for plants (min 0°C)")
    print("\nAll tests completed - program didn't crash!")

test_temperature()