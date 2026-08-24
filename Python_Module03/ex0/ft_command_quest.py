#!/usr/bin/env python3

import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    args: list[str] = sys.argv[1:]
    if len(args) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        i: int = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
