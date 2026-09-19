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

            print(f"* Battle * {c1.describe()} vs.\n{c2.describe()} now fight!")

            try:
                strategy1.act(c1)
                strategy2.act(c2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    def_strat = DefensiveStrategy()
    agr_strat = AggressiveStrategy()

    print("Tournament 0 (basic) [ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([
        (flame, normal_strat),
        (heal, def_strat)
    ])

    print("\nTournament 1 (error) [ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament([
        (flame, agr_strat),
        (heal, def_strat)
    ])

    print("\nTournament 2 (multiple) [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    tournament([
        (aqua, normal_strat),
        (heal, def_strat),
        (transform, agr_strat)
    ])
