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
    print("=== Garden Plant Growth ===")
    plant_rose = Plant("Rose", 25.0, 30)
    count_grow: float = 0.0
    plant_rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant_rose.grow(0.8)
        count_grow += 0.8
        plant_rose.age(1)
        plant_rose.show()
    print(f"Growth this week: {count_grow:.1f}cm")
