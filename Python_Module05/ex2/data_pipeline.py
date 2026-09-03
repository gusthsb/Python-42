#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._storage = list()
        self._rank = 0


    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass


    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass


    def output(self) -> tuple[int, str]:
        return (1, "o") #so para tirar o error


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()


    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for content in data:
                if not isinstance(content, str):
                    return False
            return True
        return False


    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data type for TextProcessor")
            
        if isinstance(data, str):
            self._storage.append(data)
        elif isinstance(data, list):
            for content in data:
                self._storage.append(content)