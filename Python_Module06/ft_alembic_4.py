import alchemy


def ft_alembic_4() -> None:
    print("=== Alembic 4 ===")
    print(f"Testing create_air: {alchemy.elements.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
