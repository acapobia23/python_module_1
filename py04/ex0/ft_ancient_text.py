import sys, typing

class AncientTextError(Exception):
    def __init__(self, message="Unkow AncientTextError"):
        super().__init__(message)


class AncientInputError(AncientTextError):
    def __init__(self, message="Usage: ft_ancient_text.py <file>"):
        super().__init__(message)


def read_file(file: typing.IO) -> str:
    lines = file.read()
    print("---\n")
    print(lines)
    print("---")
    return (lines)


def open_read_close_file(filename:str) -> str:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{filename}'")
        file = open(filename, "r")
        lines = read_file(file)
        file.close()
        print(f"File '{filename}' closed.\n")
        return lines


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AncientInputError
        filename = sys.argv[1]
        open_read_close_file(filename)
    except AncientInputError as e:
        print(e)
    except (FileNotFoundError, PermissionError, IsADirectoryError,
            ValueError) as e:
        print(f"Error opening file '{filename}':", e)
    