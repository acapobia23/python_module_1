class Plant:
    def __init__(self, name: str, height: float, old: int,
                 rate: float = 1) -> None:
        self.name = name
        self.height = round(height, 2)
        self.old = round(old)
        self.rate = round(rate, 2)

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.old} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.rate, 2)

    def age(self) -> None:
        self.old += 1


if __name__ == "__main__":
    ft_list = [Plant("Rose", 25.0, 30), Plant("Oak", 200.0, 365),
               Plant("Cactus", 5.0, 90), Plant("Sunflower", 80.0, 45),
               Plant("Fern", 15.0, 120)]
    i = 0
    print("=== Plant Factory Output ===")
    for flower in ft_list:
        print("Created:", end=" ")
        flower.show()
        i += 1
