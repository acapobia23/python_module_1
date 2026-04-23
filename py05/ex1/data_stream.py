from abc import ABC, abstractmethod
from typing import Any
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
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()


    print("=== Code Nexus - Data Stream === \n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    stream.register_processor(num)
    print("Send first batch of data on stream:", batch)
    stream.process_stream(batch)
    stream.print_processors_stats()
    print()
    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors:" 
          "Numeric 3, Text 2, Log 1")
    num.output()
    num.output()
    num.output()
    text.output()
    text.output()
    log.output()
    stream.print_processors_stats()
