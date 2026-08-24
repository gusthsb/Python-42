#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        temp: int = int(temp_str)
        if temp < 0:
            print(f"{temp}° is too cold for plants (min 0°)")
            raise ValueError
        return temp
    except ValueError:
        raise ValueError

def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print("Input data is '25'")
    try:
        temp: int = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except Exception as er:
        print(f"Caught input_temperature error: {er}")

    print("Input data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except Exception as er:
        print(f"Caught input_temperature error: {er}")

    print("Input data is '100'")
    try:
        temp = input_temperature("100")
    except:
        pass

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()