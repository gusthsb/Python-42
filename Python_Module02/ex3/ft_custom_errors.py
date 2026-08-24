#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as ex:
        print(f"Caught WaterError: {ex}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
