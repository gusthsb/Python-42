#!/usr/bin/env python3
import sys


def add_item(inventory: dict) -> dict:
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
                print(f"Quantity error for {key}: {ve}")
                continue
        else:
            print(f"Error - invalid parameter '{item}'")
            continue
            
    return inventory


def show_inventory() -> None:
    empty_inventory = dict()
    print("=== Inventory System Analysis ===")
    inventory = add_item(empty_inventory)
    print(f"Got inventory: {inventory}")
    print(f"item list: {list(inventory.keys())}")
    total_itens = sum(inventory.values())
    print(f"Total quantity of the {len(inventory.values())} items: {total_itens}")

 
if __name__ == "__main__":
    show_inventory()    
