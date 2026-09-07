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
            formatted_log = ": ".join(data.values())
            self._storage.append(formatted_log)
        elif isinstance(data, list):
            for content in data:
                formatted_log = ": ".join(content.values())
                self._storage.append(formatted_log)


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [item[1] for item in data]
        csv_line = ",".join(values)
        print(f"CSV Output:\n{csv_line}")


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [f'"item_{rank}": "{values}"' for rank, values in data]
        json_line = "{" + ", ".join(values) + "}"
        print(f"JSON Output:\n{json_line}")


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = list()

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            is_processed: bool = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    is_processed = True
                    break

            if not is_processed:
                print(f"DataStream error - Can't process "
                      f"element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")

        if len(self._processors) == 0:
            print("No processor found, no data")

        for processor in self._processors:
            raw_name = processor.__class__.__name__
            name = raw_name.replace("Processor", " Processor")
            remaining = len(processor._storage)
            total = remaining + processor._rank

            print(f"{name}: total {total} "
                  f"items processed, remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            data_extracted = []
            for _ in range(nb):
                if len(processor._storage) > 0:
                    data_extracted.append(processor.output())

            plugin.process_output(data_extracted)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()

    stream.register_processor(num_proc)
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message':
             'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch1}\n")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message':
             'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()
