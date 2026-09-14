import elements
from alchemy.potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (
      f"Recipe trasmuting Lead to gold: brew '{create_air()}' "
      f"and '{strength_potion()}' mixed with "
      f"'{elements.create_fire()}'"
    )
