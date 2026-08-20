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

    def get_name(self) -> str:
        return self._name

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


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.have_shade = False

    def produce_shade(self) -> None:
        self.have_shade = True

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")



class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self, value: float) -> None:
        super().grow(value)
        self.nutritional_value += 10

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += 10

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    flower_rose: Flower = Flower("Rose", 15.0, 10, "Red")
    tree_oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable_tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower_rose.show()
    print(f"[asking the {flower_rose.get_name()} to bloom]")
    flower_rose.bloom()
    flower_rose.show()

    print("=== Tree")
    tree_oak.show()
    print(f"[asking the {tree_oak.get_name()} to produce shade]")
    tree_oak.produce_shade()
    tree_oak.show()
    tree_oak.produce_shade()
    print(f"Tree {tree_oak.get_name()} now produces a shade of {tree_oak.get_height()}cm"
          f" long and {tree_oak.trunk_diameter}cm wide.")

    print("=== Vegetable")
    vegetable_tomato.show()
    print("[make tomato grow and age for 20 days]")
    vegetable_tomato.grow(42)
    vegetable_tomato.age(20)
    vegetable_tomato.show()
