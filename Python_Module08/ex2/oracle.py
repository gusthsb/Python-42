#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def access_mainframe() -> None:
    load_dotenv()
    data_base_url: str | None = os.getenv("DATABASE_URL")
    oracle_key: str | None = os.getenv("ORACLE_KEY")
    status: str | None = os.getenv("MAINFRAME_STATUS")

    if not data_base_url or not oracle_key:
        print("Error environments variables are missing.")
        print("Verify if the .env is nice configured.")
        return

    print(f"Mainframe: {status}")
    print(f"Database: {data_base_url}")
    print(f"Oracle key: {'*' * 8}...")
    print("\nSucess connection established!")


if __name__ == "__main__":
    access_mainframe()