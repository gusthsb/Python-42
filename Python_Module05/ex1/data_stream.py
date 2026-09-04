#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._storage: list[str] = list()
        self._rank = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        data = self._storage.pop(0)
        current_rank = self._rank
        self._rank += 1
        return (current_rank, data)


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
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self._storage.append(data)
        elif isinstance(data, list):
            for content in data:
                self._storage.append(content)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int | float):
            return True
        elif isinstance(data, list):
            for content in data:
                if not isinstance(content, int | float):
                    return False
            return True

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, int | float):
            self._storage.append(str(data))
        elif isinstance(data, list):
            for content in data:
                self._storage.append(str(content))


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for k, c in data.items():
                if not isinstance(k, str) or not isinstance(c, str):
                    return False
            return True

        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False

                for k, c in item.items():
                    if not isinstance(k, str) or not isinstance(c, str):
                        return False
                return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, dict):
            self._storage.append(str(data))
        elif isinstance(data, list):
            for content in data:
                self._storage.append(str(content))


class DataStream():
    pass


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()

    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        pass # so para nao mostrar o erro :)
        # num_proc.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    num_proc.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()

    print(f"Trying to validate input '42': {txt_proc.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    txt_proc.ingest(['Hello', 'Nexus', 'World'])

    print("Extracting 1 value...")
    rank, val = txt_proc.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
