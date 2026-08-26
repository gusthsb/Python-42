#!/usr/bin/env python3
import random


def gen_player_achievements() -> set:
    achievements = [
    "Crafting Genius", "World Savior", "Master Explorer", 
    "Collector Supreme", "Untouchable", "Boss Slayer", 
    "Strategist", "Speed Runner", "Survivor", 
    "Treasure Hunter", "First Steps", "Sharp Mind", "Unstoppable"
    ]
    len_achievements = random.randint(0, len(achievements))
    player_achievements = random.sample(achievements, k = len_achievements)
    return set(player_achievements)


def show_achievements() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievement: {set.difference(alice, bob, charlie, dylan)}")
    print(f"Common achievement: {alice & bob & charlie & dylan}")
    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - bob - alice - dylan}")
    print(f"Only Dylan has: {dylan - bob - charlie - alice}\n")
    all_achievements = set.union(alice, bob, charlie, dylan)
    print(f"Alice is missing: {alice - all_achievements}")
    print(f"Bob is missing: {bob - all_achievements}")
    print(f"Charlie is missing: {charlie - all_achievements}")
    print(f"Dylan is missing: {dylan - all_achievements}")


if __name__ == "__main__":
    show_achievements()
