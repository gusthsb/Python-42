#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        pos_input: str = input("Enter new coordinates as floats "
                          "in format 'x,y,z': ")
        input_parts: list[str] = pos_input.split(',')
        if len(input_parts) != 3:
            print("Invalid syntax")
            continue
        try:
            coords = [float(val.strip()) for val in input_parts]
            return (coords[0], coords[1], coords[2])
        except ValueError as ve:
            print(f"Error on parameter: {ve}")
            continue


def show_coordinate() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]:.1f}, Y={pos1[1]:.1f}, Z={pos1[2]:.1f}")
    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {dist_center:.4f}\n")   
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    distance_p2_p1 = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {distance_p2_p1:.4f}")


if __name__ == "__main__":
    show_coordinate()
