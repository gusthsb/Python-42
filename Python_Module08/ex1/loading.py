#!/usr/bin/env python3
import sys


try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError as e:
    print("Required data libraries are missing...")
    print("System details: {e}")
    print("Please run: pip install -r requirements.txt\n")
    sys.exit(1)


def load_data() -> pd.DataFrame | None:
    try:
        goals_scored = np.random.randint(0, 5, 10)
        goals_conceded = np.random.randint(0, 3, 10)
        raw_data = np.column_stack((goals_scored, goals_conceded))
        data_frame = pd.DataFrame(raw_data, columns=['Goals_Scored', 'Goals_Conceded'])
        data_frame.index = [f"Match {i+1}" for i in range(10)]
        print(f"Loading dataset of dimensions {data_frame.shape}")
        return data_frame

    except Exception as e:
        print("An unexpected error occurred: {e}")
        return None


def data_visualization(data_frame: pd.DataFrame) -> None:
    try:
        data_frame.plot(
            title="Brazilian National Team Performance (10 matches)",
            figsize=(10, 5),
            marker='o',
            color=['green','red']
        )

        plt.xlabel("Matches")
        plt.ylabel("Amount of Goals")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    except Exception as e:
        print(f"An unexpected error occurred during visualization: {e}")


if __name__ == "__main__":
    print("=== Brazilian National Futebol Team ===")
    data = load_data()
    if data is not None:
        print("\nHead of first matches:")
        print(data.head())

        print("\n== Opening Chart ==")
        data_visualization(data)