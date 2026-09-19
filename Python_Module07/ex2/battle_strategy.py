from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilites import HealCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self) -> None:
        super().__init__()  

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' "
                             f"for this defensive strategy")
    

class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' "
                             f"for this normal strategy")


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid creature '{creature.name}' "
                             f"for this agressive strategy")
