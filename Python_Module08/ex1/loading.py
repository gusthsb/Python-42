#!/usr/bin/env python3
import sys
from importlib import import_module
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import pandas as pd

PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "requests": "Network access",
    "matplotlib": "Visualization",
}
OUTPUT_FILE = "matrix_analysis.png"


def check_dependencies() -> bool:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_ok = True
    for name, role in PACKAGES.items():
        try:
            module = import_module(name)
            ver = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({ver}) - {role} ready")
        except ImportError:
            print(f"[KO] {name} - {role} is not ready")
            all_ok = False

    print()
    return all_ok


def load_data() -> "pd.DataFrame | None":
    import pandas as pd
    import numpy as np

    try:
        print("Analyzing Brazil data...")
        print("Processing data points...")

        goals_scored = np.random.randint(0, 5, 10)
        goals_conceded = np.random.randint(0, 3, 10)
        raw_data = np.column_stack((goals_scored, goals_conceded))

        data_frame = pd.DataFrame(
            raw_data, columns=['Goals_Scored', 'Goals_Conceded'])
        data_frame.index = pd.Index([f"Match {i+1}" for i in range(10)])

        print(f"Loading dataset of dimensions {data_frame.shape}")
        return data_frame

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def data_visualization(data_frame: "pd.DataFrame") -> None:
    import matplotlib.pyplot as plt

    try:
        print("Generating visualization...")

        data_frame.plot(
            title="Brazilian National Team Performance (10 matches)",
            figsize=(10, 5),
            marker='o',
            color=['green', 'red']
        )

        plt.xlabel("Matches")
        plt.ylabel("Amount of Goals")
        plt.grid(True, linestyle='--', alpha=0.7)

        plt.savefig(OUTPUT_FILE)

        print("\nAnalysis complete!")
        print(f"Results saved to: {OUTPUT_FILE}")

    except Exception as e:
        print(f"An unexpected error occurred during visualization: {e}")


if __name__ == "__main__":
    if not check_dependencies():
        print("WARNING: Required data libraries are missing.")
        print("Please run: poetry install")
        sys.exit(1)

    print("=== Brazilian National Football Team ===")
    data = load_data()

    if data is not None:
        print("\nHead of first matches:")
        print(data.head())

        print("\n== Opening Chart ==")
        data_visualization(data)
