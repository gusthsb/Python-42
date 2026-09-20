from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


def test_healing_factory(
    factory: HealingCreatureFactory, b_name: str, e_name: str
) -> None:
    """
    Testing creations, discriptions, attacks and heals of the creatures
    """
    base_creature = factory.create_base(b_name)
    evolved_creature = factory.create_evolved(e_name)
    print("Testing Creature with healing capability\n base:")

    print(base_creature.describe())
    print(base_creature.attack())

    if isinstance(base_creature, HealCapability):
        print(base_creature.heal())

    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())

    if isinstance(evolved_creature, HealCapability):
        print(evolved_creature.heal())


def test_transform_factory(
    factory: TransformCreatureFactory, b_name: str, e_name: str
) -> None:
    """
    Testing creations, discriptions, attacks and transform of the creatures
    """
    base_creature = factory.create_base(b_name)
    evolved_creature = factory.create_evolved(e_name)

    print("\nTesting Creature with transform capability")
    print(" base:")

    print(base_creature.describe())
    print(base_creature.attack())

    if isinstance(base_creature, TransformCapability):
        print(base_creature.transform())

    print(base_creature.attack())

    if isinstance(base_creature, TransformCapability):
        print(base_creature.revert())

    print(" evolved:")

    print(evolved_creature.describe())
    print(evolved_creature.attack())
    if isinstance(evolved_creature, TransformCapability):
        print(evolved_creature.transform())

    print(evolved_creature.attack())

    if isinstance(evolved_creature, TransformCapability):
        print(evolved_creature.revert())


if __name__ == "__main__":
    nlist = ["Sproutling", "Bloomelle", "Shiftling", "Morphagon"]
    test_healing_factory(HealingCreatureFactory(), nlist[0], nlist[1])
    test_transform_factory(TransformCreatureFactory(), nlist[2], nlist[3])
