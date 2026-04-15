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


def modify_data(lines: str) -> str:
        lines = lines.replace("\n", "#\n")
        print("---\n")
        print(lines)
        print("---")
        return lines

def create_new_file(filename: str) -> None:
    if filename:
        file = open(filename, "w")
        print(f"Saving data to '{filename}'")
        file.write(lines)
        print(f"Data saved in file '{filename}'")
        file.close()
    else:
        print("Not saving data.")
    print()

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AncientInputError
        filename = sys.argv[1]
        lines = open_read_close_file(filename)
        print("\nTransform data:\n")
        lines = modify_data(lines)
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        filename = sys.stdin.readline().rstrip("\n")
        create_new_file(filename)
    except AncientInputError as e:
        sys.stderr.write(f"[STDERR] {e}\n")
    except (FileNotFoundError, PermissionError, IsADirectoryError,
            ValueError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")