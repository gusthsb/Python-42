import sys


try:
    import pandas as pd
    import numpy as np
    import matplotlib as plt
except ImportError as e:
    print("Required data libraries are missing...")
    print("System details: {e}")
    print("Please run:")
    print("pip install -r requirements.txt\n")
    sys.exit(1)


def load_data(path: str) -> None:
    pass