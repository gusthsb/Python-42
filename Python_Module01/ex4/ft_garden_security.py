#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name.capitalize()}: {self._height:.1f}cm,"
              f" {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name.capitalize()}: Error, height"
                  f" can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age"
                  f" can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age

    def grow(self, value: float) -> None:
        current_height = self.get_height()
        self.set_height(current_height + value)

    def age(self, days: int) -> None:
        current_age = self.get_age()
        self.set_age(current_age + days)


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant.show()

    plant.set_height(25.0)
    print("Height updated: 25cm")
    plant.set_age(30)
    print("Age updated: 30 days")

    plant.set_height(-5.0)
    plant.set_age(-10)
    print("Current state: ", end="")
    plant.show()
