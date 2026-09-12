import alchemy


def ft_alembic_4() -> None:
    print("=== Alembic 4 ===")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth:")

    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError as e:
        print("Traceback (most recent call last):")
        print(" ...")
        print(f"AttributeError: {e}")
