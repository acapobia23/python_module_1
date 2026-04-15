def secure_archive(filename: str, mode: int,
                   new_text: str = "") -> tuple[bool, str]:
    try:
        if mode == 0:
            with open(filename, "r") as file:
                lines = file.read()
                state = True
        elif mode == 1:
            with open(filename, "w") as file:
                file.write(new_text)
                state = True
                lines = new_text
    except (FileNotFoundError, PermissionError) as e:
        state = False
        lines = str(e)
    except (IsADirectoryError, ValueError) as e:
        state = False
        lines = str(e)
    return (state, lines)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive'to read from a nonexistent file:")
    archive = secure_archive("/not/existing/file", 0)
    print(archive)

    print()

    print("Using 'secure_archive'to read from an inaccessible file:")
    archive = secure_archive("inaccessible.txt", 0)
    print(archive)

    print()

    print("Using 'secure_archive'to read from a regular file:")
    archive = secure_archive("ancient_fragment.txt", 0)
    print(archive)

    print()

    new_text = "Content successfully written to file"
    print("Using 'secure_archive'to write previous content to a new file:")
    archive = secure_archive("ancient_fragment.txt", 1, new_text)
    print(archive)
    print()
