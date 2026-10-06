#!/usr/bin/env python3
import alchemy.grimoire


def ft_kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    extracted_record: str = alchemy.grimoire.light_spell_record(
        'Fantasy', 'Earth, wind and fire'
    )
    print(f"Testing record light spell: {extracted_record}")


if __name__ == "__main__":
    ft_kaboom_0()
