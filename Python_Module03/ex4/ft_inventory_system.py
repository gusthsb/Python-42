#!/usr/bin/env python3
import sys


def add_item(inventory: dict[str, int]) -> dict[str, int]:
    args = sys.argv[1:]
    for item in args:
        if ":" in item:
            key, value = item.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in inventory:
                print(f"Redundant item '{key}' - discarding")
                continue
            try:
                inventory[key] = int(value)
            except ValueError as ve:
                print(f"Quantity error for '{key}': {ve}")
                continue
        else:
            print(f"Error - invalid parameter '{item}'")
            continue

    return inventory


def show_inventory() -> None:
    empty_inventory: dict[str, int] = dict()
    print("=== Inventory System Analysis ===")
    inventory = add_item(empty_inventory)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    if inventory:
        total_itens = sum(inventory.values())
        print(f"Total quantity of the {len(inventory.values())}"
              f" items: {total_itens}")
        for key in inventory:
            value = inventory[key]
            percent = round((value / total_itens) * 100, 1)
            print(f"item {key} represents {percent}%")
        most_abundant = list(inventory.keys())[0]
        least_abundant = list(inventory.keys())[0]
        for key in inventory:
            if inventory[key] > inventory[most_abundant]:
                most_abundant = key
            if inventory[key] < inventory[least_abundant]:
                least_abundant = key
        print(f"Item most abundant: {most_abundant} with quantity"
              f" {inventory[most_abundant]}")
        print(f"Item least abundant: {least_abundant} with quantity"
              f" {inventory[least_abundant]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    show_inventory()
