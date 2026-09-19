from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy as bs
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def tournament(opponents: list[tuple[CreatureFactory, bs]]) -> None:
    print(f"*** Tournament *** {len(opponents)} opponents involved")

    creature_names = {
        "FlameFactory": "Flameling",
        "AquaFactory": "Aquabub",
        "HealingCreatureFactory": "Sproutling",
        "TransformCreatureFactory": "Shiftling"
    }

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            n1 = creature_names.get(factory1.__class__.__name__, "Unknown")
            n2 = creature_names.get(factory2.__class__.__name__, "Unknown")

            c1 = factory1.create_base(n1)
            c2 = factory2.create_base(n2)