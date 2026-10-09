#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex0.creatures import Creature


def test_factory(factory: CreatureFactory, b_name: str, e_name: str) -> None:
    """
    Tests whether a factory can create base and evolve creatures,
    print their description and attacks
    """
    print("Testing factory")
    base_creature: Creature = factory.create_base(b_name)
    evolved_creature: Creature = factory.create_evolved(e_name)
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def base_battle(factory1: CreatureFactory, factory2: CreatureFactory,
                b1_name: str, b2_name: str) -> None:
    """
    Make a battle with two bases creatures
    """
    b1_creature: Creature = factory1.create_base(b1_name)
    b2_creature: Creature = factory2.create_base(b2_name)
    print("Testing battle")
    print(b1_creature.describe())
    print("vs.")
    print(b2_creature.describe())
    print("fight!")
    print(b1_creature.attack())
    print(b2_creature.attack())


if __name__ == "__main__":
    test_factory(FlameFactory(), "Flameling", "Pyrodon")
    test_factory(AquaFactory(), "Aquabub", "Torragon")
    base_battle(FlameFactory(), AquaFactory(), "Flameling", "Aquabub")
