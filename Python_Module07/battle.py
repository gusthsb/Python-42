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

test_factory(FlameFactory(), "Flameling", "Pyrodon")