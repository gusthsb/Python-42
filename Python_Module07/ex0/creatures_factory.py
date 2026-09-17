from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_base(self, name: str) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self, name: str) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self, name: str) -> Creature:
        return Flameling(name)

    def create_evolved(self, name: str) -> Creature:
        return Pyrodon(name)


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self, name: str) -> Creature:
        return Aquabub(name)

    def create_evolved(self, name: str) -> Creature:
        return Torragon(name)
