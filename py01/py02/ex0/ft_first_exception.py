def input_temperature(temp_str :str) -> int:
        return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
      print(f"Temperature is now {input_temperature("25")}°C")
    except ValueError as e:
        print(e)
    print("Input data is 'abc'")
    try:
      input_temperature("abc")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nAll tests completed - program didn't crash!")
