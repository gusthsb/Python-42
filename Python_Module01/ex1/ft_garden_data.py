#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm,"
              f" {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant = Plant("Rose", 25, 30)
    plant1 = Plant("Sunflower", 80, 45)
    plant2 = Plant("cactus", 15, 120)
    plant.show()
    plant1.show()
    plant2.show()
