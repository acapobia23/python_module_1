from abc import ABC, abstractmethod
from typing import Any, Protocol
import typing

class DataError(Exception):
    def __init__(self, message:str = "Storage is empty"):
        super().__init__(message)


class DataNumericError(DataError):
    def __init__(self, message:str = "Improper numeric data"):
        super().__init__(message)


class DataTextError(DataError):
    def __init__(self, message:str = "Improper text data"):
        super().__init__(message)


class DataLogError(DataError):
    def __init__(self, message:str = "Improper log data"):
        super().__init__(message)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class ExportCsv:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output\n" + ",".join(v for _, v in data))


class ExportJson:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:\n"+ 
              "{" + " ,".join(f'"item_{k}": "{v}"' for k,v in data) + "}")

class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass
    
    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise DataError
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        self.storage = []
        self.rank = 0
        self.tot_processed = 0

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for value in data:
                if not isinstance(value, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if self.validate(data) is False:
            raise DataNumericError
        if isinstance(data, (int, float)):
            self.storage.append((self.rank ,str(data)))
            self.rank += 1
            self.tot_processed += 1
        else:
            for value in data:
                self.storage.append((self.rank, str(value)))
                self.rank += 1
                self.tot_processed += 1


class TextProcessor(DataProcessor):
    def __init__(self):
        self.storage = []
        self.rank = 0
        self.tot_processed = 0

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for value in data:
                if not isinstance(value, str):
                    return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if self.validate(data) is False:
            raise DataTextError
        if isinstance(data, str):
            self.storage.append((self.rank ,data))
            self.rank += 1
            self.tot_processed += 1
        else:
            for x in data:
                self.storage.append((self.rank, x))
                self.rank += 1
                self.tot_processed += 1


class LogProcessor(DataProcessor):
    def __init__(self):
        self.storage = []
        self.rank = 0
        self.tot_processed = 0

    def validate(self, data: typing.Any) -> bool:
        if not isinstance(data, ( dict, list)):
            return False
        elif isinstance(data, list):
            for value in data:
                if not isinstance(value, dict):
                    return False
        return True

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise DataLogError

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise DataLogError

        if isinstance(data, dict):
            tmp = data.get("log_level") + ": " + data.get("log_message")
            self.storage.append((self.rank, tmp))
            self.rank += 1
            self.tot_processed += 1
        else:
            for dicts in data:
                tmp = dicts.get("log_level") + ": " + dicts.get("log_message")
                self.storage.append((self.rank, tmp))
                self.rank += 1
                self.tot_processed += 1


class DataStream:
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if self.processors and stream:
            for elem in stream:
                flag = False
                for proc in self.processors:
                    if proc.validate(elem):
                        proc.ingest(elem)
                        flag = True
                        break
                if not flag:
                    print("DataStream error - Can't process element in stream:", elem)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        for p in self.processors:
            name = p.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: "
                f"total {p.tot_processed} items processed," 
                f"remaining {len(p.storage)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            items = []
            for _ in range(nb):
                try:
                    items.append(proc.output())
                except DataError:
                    break
            plugin.process_output(items)



if __name__ == "__main__":
    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")

    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print("Send first batch of data on stream:", batch, "\n")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, ExportCsv())
    print()
    stream.print_processors_stats()
    batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
        {"log_level": "ERROR", "log_message": "500 server crash"},
        {"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"}
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("\nSend another batch of data:", batch, "\n")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, ExportJson())
    print()
    stream.print_processors_stats()
