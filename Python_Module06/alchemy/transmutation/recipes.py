import elements
from alchemy.potions import strength_potion as sp
from ..elements import create_air as ca


def lead_to_gold() -> str:
   return f"Recipe transmuting Lead to Gold: brew '{ca()}' and '{sp()}' mixed with '{elements.create_fire()}'"

lead_to_gold()