#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm,"
              f" {self.plant_age} days old")

    def grow(self, value: float) -> None:
        self.height += value

    def age(self, days: int) -> None:
        self.plant_age += days


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()
