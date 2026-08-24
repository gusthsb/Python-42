#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "Ola" + 42
    else:
        pass


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully\n")
        except ValueError as vs:
            print(f"Caught ValueError: {vs}")
        except ZeroDivisionError as zd:
            print(f"Caught ZeroDivisionError: {zd}")
        except FileNotFoundError as fn:
            print(f"Caught FileNotFoundError: {fn}")
        except TypeError as te:
            print(f"Caught TypeError: {te}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
