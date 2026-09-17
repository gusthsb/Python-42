from abc import ABC, abstractmethod
from ex0 import CreatureFactory
from ex0.creatures import Creature
from creatures import Sproutling, Bloomelle

class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class HealCapability(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def heal(self) -> str:
        pass


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self, name: str) -> Creature:
        return Sproutling(name)

    def create_evolved(self, name: str) -> Creature:
        return Bloomelle(name)


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self, name: str) -> Creature:
        return Sproutling(name)

    def create_evolved(self, name: str) -> Creature:
        return Bloomelle(name)
