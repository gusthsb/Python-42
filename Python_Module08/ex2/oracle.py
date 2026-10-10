#!/usr/bin/env python3
import os
import sys

try:
    from dotenv import load_dotenv # type: ignore
except ImportError:
    print("ERROR: python-dotenv is not installed.")
    print("Please run: pip install python-dotenv")
    sys.exit(1)


def access_mainframe() -> None:
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    mode: str = os.getenv("MATRIX_MODE", "development").lower()
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")

    default_log = "DEBUG" if mode == "development" else "WARNING"
    log_level: str = os.getenv("LOG_LEVEL", default_log).upper()

    missing: list[str] = []
    if not db_url:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if not zion_endpoint:
        missing.append("ZION_ENDPOINT")

    print("=== Configuration Loaded ===")
    print(f"Matrix Mode   : {mode.upper()}")
    print(f"Log Level     : {log_level}")
    print(f"Zion Endpoint : {zion_endpoint if zion_endpoint else 'MISSING'}")
    print("-" * 30)

    if mode == "production":
        print("[PRODUCTION ENVIRONMENT]")
        print("Security: STRICT (Secrets are hidden)")

        if missing:
            print(f"\nCRITICAL ERROR: Missing required variables "
                  f"for production: {', '.join(missing)}")
            print("Action aborted to prevent system exposure.")
            sys.exit(1)

        print("Database URL  : *** PROTECTED ***")
        print("API Key       : *** PROTECTED ***")

    else:
        print("[DEVELOPMENT ENVIRONMENT]")
        print("Security: RELAXED (Secrets are visible for debugging)")

        if missing:
            print(f"Warning: Missing variables: {', '.join(missing)}")

        print(f"Database URL  : {db_url if db_url else 'Not Set'}")
        print(f"API Key       : {api_key if api_key else 'Not Set'}")

    print("\n[SUCCESS] The Oracle sees all configurations.")


if __name__ == "__main__":
    access_mainframe()
