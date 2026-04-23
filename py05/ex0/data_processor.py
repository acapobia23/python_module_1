from abc import ABC, abstractmethod
from typing import Any

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
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    
    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise DataError
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        self.storage = []
        self.rank = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for value in data:
                if not isinstance(value, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise DataNumericError
        if isinstance(data, (int, float)):
            self.storage.append((self.rank ,str(data)))
            self.rank += 1
        else:
            for value in data:
                self.storage.append((self.rank, str(value)))
                self.rank += 1


class TextProcessor(DataProcessor):
    def __init__(self):
        self.storage = []
        self.rank = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for value in data:
                if not isinstance(value, str):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise DataTextError
        if isinstance(data, str):
            self.storage.append((self.rank ,data))
            self.rank += 1
        else:
            for x in data:
                self.storage.append((self.rank, x))
                self.rank += 1


class LogProcessor(DataProcessor):
    def __init__(self):
        self.storage = []
        self.rank = 0

    def validate(self, data: Any) -> bool:
        if not isinstance(data, ( dict, list)):
            return False
        elif isinstance(data, list):
            for value in data:
                if not isinstance(value, dict):
                    return False
        return True

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise DataLogError

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise DataLogError

        if isinstance(data, dict):
            tmp =  data.get("log_level") + ": " + data.get("log_message")
            self.storage.append((self.rank, tmp))
            self.rank += 1
        else:
            for dicts in data:
                tmp = dicts.get("log_level") + ": " + dicts.get("log_message")
                self.storage.append((self.rank, tmp))
                self.rank += 1


def numeric_test() -> None:
    num = NumericProcessor()
    print(" Trying to validate input '42':", num.validate(42))
    print(" Trying to validate input 'hello':", num.validate("hello"))
    try:        
        print(" Test invalid ingestion of string 'foo'without prior validation:")
        num.ingest("foo")
    except (DataError, DataNumericError) as e:
        print(" Got exception:", e)
    print(" Processing data: [1, 2, 3, 4, 5]")
    num.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for x in range(3):
        value = num.output()
        print(f" Numeric value {value[0]}:{value[1]}")
        

def text_test() -> None:
    text = TextProcessor()
    print(" Trying to validate input '42':", text.validate(42))
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    try:
        text.ingest(['Hello', 'Nexus', 'World'])
        print(" Extracting 1 value...")
        value = text.output()
        print(f" Text value {value[0]}: {value[1]}")
    except (DataError, DataTextError) as e:
        print(" Got exception:", e)


def log_test() -> None:
    log = LogProcessor()
    test = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]

    print(" Trying to validate input 'Hello':", log.validate("hello"))
    print(" Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},"
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    try:
        log.ingest(test)
        print(" Extracting 2 values...")
        for i in range(2):
            value = log.output()
            print(f" Log entry {value[0]}: {value[1]}")
            
    except (DataError, DataLogError) as e:
        print(" Got exception:", e)


def test_case() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    numeric_test()
    print()
    print("Testing Text Processor...")
    text_test()
    print()
    print("Testing Log Processor...")
    log_test()
    print()

if __name__ == "__main__":
    test_case()