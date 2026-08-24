#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)\n")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)\n")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    print("Input data is '25'")
    try:
        temp: int = input_temperature("25")
        print(f"Temperature is now {temp}°C\n")
    except Exception as er:
        print(f"Caught input_temperature error: {er}\n")

    print("Input data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C\n")
    except Exception as er:
        print(f"Caught input_temperature error: {er}\n")

    print("Input data is '100'")
    try:
        temp = input_temperature("100")
    except Exception as er:
        print(f"Caught input_temperature error: {er}")

    print("Input data is '-50'")
    try:
        temp = input_temperature("-50")
    except Exception as er:
        print(f"Caught input_temperature error: {er}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
