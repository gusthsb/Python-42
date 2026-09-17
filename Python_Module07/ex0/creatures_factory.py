from abc import ABC, abstractmethod
import typing


class CreatureFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> None:
        return super().create_base()

    def create_evolved(self) -> None:
        return super().create_evolved()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> None:
        return super().create_base()

    def create_evolved(self) -> None:
        return super().create_evolved()
