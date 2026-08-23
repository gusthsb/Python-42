#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self.stat_grow = 0
        self.stat_age = 0
        self.stat_show = 0

    def show(self) -> None:
        self.stat_show += 1
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
        self.stat_grow += 1
        current_height = self.get_height()
        self.set_height(current_height + value)

    def age(self, days: int) -> None:
        self.stat_age += 1
        current_age = self.get_age()
        self.set_age(current_age + days)

    def display_stats(self) -> None:
        print(f"Stats: {self.stat_grow} grow, {self.stat_age} age,"
              f"{self.stat_show} show")

    @staticmethod
    def check_year_old(age: int) -> bool:
        if age < 365:
            return False
        else:
            return True

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
        self.stat_shade = 0

    def produce_shade(self) -> None:
        self.stat_shade += 1
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}cm"
              f" long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_stats(self) -> None:
        super().display_stats()
        print(f" {self.stat_shade} shade")


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

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seeds(Flower):

    def __init__(self, name: str, height: float, age: int, color: str,
                 seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def get_seed(self) -> int:
        return self._seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


if __name__ == "__main__":
    flower_rose: Flower = Flower("Rose", 15.0, 10, "red")
    tree_oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    sunflower_seed: Seeds = Seeds("Sunflower", 80.0, 45, "yellow", 0)
    anonymous_plant: Plant = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year_old(400)}")

    print("\n=== Flower")
    flower_rose.show()
    print(f"[statistics for {flower_rose.get_name()}]")
    flower_rose.display_stats()
    print("[asking the rose to grow and bloom]")
    flower_rose.grow(8.0)
    flower_rose.bloom()
    flower_rose.show()
    print(f"[statistics for {flower_rose.get_name()}]")
    flower_rose.display_stats()
    print("\n=== Tree")
    tree_oak.show()
    print(f"[statistics for {tree_oak.get_name()}]")
    tree_oak.display_stats()
    print("[asking the oak to produce shade]")
    tree_oak.produce_shade()
    print(f"[statistics for {tree_oak.get_name()}]")
    tree_oak.display_stats()
    print("\n=== Seed")
    sunflower_seed.show()
    print("[make sunflower grow, age and bloom]")
    sunflower_seed.grow(30.0)
    sunflower_seed.age(20)
    sunflower_seed.bloom()
    sunflower_seed._seeds = 42
    sunflower_seed.show()
    print(f"[statistics for {sunflower_seed.get_name()}]")
    sunflower_seed.display_stats()
    print("\n=== Anonymous")
    anonymous_plant.show()
    print(f"[statistics for {anonymous_plant.get_name()}]")
    anonymous_plant.display_stats()
    print("")
