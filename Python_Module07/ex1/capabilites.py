from abc import ABC, abstractmethod


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