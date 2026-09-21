import sys
import os


def on_venv() -> bool:
    return sys.prefix != sys.base_prefix


def py_path() -> str:
    return f"Current Python: {sys.executable}"


def check_venv_name() -> str:
    if on_venv():
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
        return f"Virtual Environment: {venv_name}"
    else:
        return f"Virtual Environment: None detected"


if __name__ == "__main__":
    if on_venv():
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"{py_path()}")
        print(f"{check_venv_name()}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print(f"Package installation path: {sys.path[-1]}")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"{py_path()}")
        print(f"{check_venv_name()}\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows\n")
        print("Then run this program again.")
