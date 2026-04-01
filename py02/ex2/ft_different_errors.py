def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42 / 0  
    elif operation_number == 2:
        open("c4p0_file.txt")
    elif operation_number == 3:
        "ollare" + 8
    else:
        return

def test_error_types():
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print("Caught ValueError:", e)
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)
        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)
        except TypeError as e:
            print("Caught TypeError:", e)
    print("\nAll error types tested successfully!")

test_error_types()    