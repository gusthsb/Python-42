#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy as bs
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def tournament(opponents: list[tuple[CreatureFactory, bs]]) -> None:
    print(f"*** Tournament *** {len(opponents)} opponents involved")

    creature_names: dict[str, str] = {
        "FlameFactory": "Flameling",
        "AquaFactory": "Aquabub",
        "HealingCreatureFactory": "Sproutling",
        "TransformCreatureFactory": "Shiftling",
    }

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            base_name1: str = creature_names.get(
                factory1.__class__.__name__, "Unknown")
            base_name2: str = creature_names.get(
                factory2.__class__.__name__, "Unknown")

            base_creature1: Creature = factory1.create_base(base_name1)
            base_creature2: Creature = factory2.create_base(base_name2)

            print(f"* Battle * {base_creature1.describe()} "
                  f"vs.\n{base_creature2.describe()} now fight!")

            try:
                strategy1.act(base_creature1)
                strategy2.act(base_creature2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame: FlameFactory = FlameFactory()
    aqua: AquaFactory = AquaFactory()
    heal: HealingCreatureFactory = HealingCreatureFactory()
    transform: TransformCreatureFactory = TransformCreatureFactory()
    normal_strat: NormalStrategy = NormalStrategy()
    def_strat: DefensiveStrategy = DefensiveStrategy()
    agr_strat: AggressiveStrategy = AggressiveStrategy()

    print("Tournament 0 (basic) [ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([(flame, normal_strat), (heal, def_strat)])

    print("\nTournament 1 (error) [ \n"
          " (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament([(flame, agr_strat), (heal, def_strat)])

    print(
        "\nTournament 2 (multiple) [ (Aquabub+Normal), "
        "(Healing+Defensive), (Transform+Aggressive) ]"
    )
    tournament([(aqua, normal_strat), (heal, def_strat),
                (transform, agr_strat)])
