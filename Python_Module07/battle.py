from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory, b_name: str, e_name: str) -> None:
    """
    Tests whether a factory can create base and evolve creatures, and
    print their description and attacks
    """
    print("Testing factory")
    base_creature = factory.create_base(b_name)
    evolved_creature = factory.create_evolved(e_name)
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def base_battle(
    factory1: CreatureFactory, factory2: CreatureFactory, 
    b1_name: str, b2_name: str) -> None:
    """
    Make a battle with two bases creatures
    """
    b1_creature = factory1.create_base(b1_name)
    b2_creature = factory2.create_base(b2_name)
    print("Testing battle")
    print(b1_creature.describe())
    print("vs.")
    print(b2_creature.describe())
    print("fight!")
    print(b1_creature.attack())
    print(b2_creature.attack())


if __name__ == "__main__":
    test_flame_creature = test_factory(FlameFactory(), "Flameling", "Pyrodon")
    test_aqua_creature = test_factory(AquaFactory(), "Aquabub", "Torragon")
    base_battle(FlameFactory(), AquaFactory(), "Flameling", "Aquabub")
