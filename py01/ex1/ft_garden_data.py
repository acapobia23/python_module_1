class Plant:
    def __init__(self, name: str, height: float, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old

    def show(self) ->None:
        print(f"{self.name}: {self.height}cm, {self.old} days old")


if __name__ == "__main__":
    first = Plant("Rose", 25.0, 30)
    second = Plant("Sunflower", 80.0, 45)
    third = Plant("Cactus", 15.0, 120)

    print("=== Garden Plant Registry ===")
    first.show()
    second.show()
    third.show()
