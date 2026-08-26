#!/usr/bin/env python3
import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    len_achievements = random.randint(0, len(achievements))
    player_achievements = random.sample(achievements, k=len_achievements)
    return set(player_achievements)


def show_achievements() -> None:
    achievements: list[str] = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind", "Unstoppable"
        ]
    set_achievements: set[str] = set(achievements)
    print("=== Achievement Tracker System ===\n")
    alice: set[str] = gen_player_achievements(achievements)
    bob: set[str] = gen_player_achievements(achievements)
    charlie: set[str] = gen_player_achievements(achievements)
    dylan: set[str] = gen_player_achievements(achievements)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievement:"
          f"{set.union(alice, bob, charlie, dylan)}")
    print(f"Common achievement: {alice & bob & charlie & dylan}\n")
    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - bob - alice - dylan}")
    print(f"Only Dylan has: {dylan - bob - charlie - alice}\n")
    print(f"Alice is missing: {set_achievements - alice}")
    print(f"Bob is missing: {set_achievements - bob}")
    print(f"Charlie is missing: {set_achievements - charlie}")
    print(f"Dylan is missing: {set_achievements - dylan}")


if __name__ == "__main__":
    show_achievements()
