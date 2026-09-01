#!/usr/bin/env python3

import sys
import typing


def checking_arg() -> None:
    argv = sys.argv
    read_content: str = ""
    if len(argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name: str = argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{argv[1]}'")
    try:
        file_opening: typing.IO = open(file_name)
        print("---\n")
        read_content = file_opening.read()
        print(read_content, end="")
        print("\n---")
        file_opening.close()
        print(f"File '{file_name}' closed.\n")
        print("Transform data:")
        print("---\n")
        splited_line: list[str] = read_content.split('\n')
        processed_line: list[str] = [
            line + "#" if line != "" else line for line in splited_line
        ]
        last_text: str = '\n'.join(processed_line)
        print(last_text, end="")
        print("\n---")
        new_file_name: str = input("Enter new file name (or empty): ")
        if new_file_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file_name}'")
            new_file: typing.IO = open(new_file_name, 'w')
            new_file.write(last_text)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.")
    except FileNotFoundError as fe:
        print(f"Error opening file '{file_name}': {fe}")
    except PermissionError as pe:
        print(f"Error opening file '{file_name}': {pe}")


if __name__ == "__main__":
    checking_arg()
