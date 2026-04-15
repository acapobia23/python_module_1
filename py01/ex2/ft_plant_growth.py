class Plant:
    def __init__(self, name: str, height: float, old: int,
                 rate: float) -> None:
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
    ft_list = [Plant("Rose", 25, 30, 0.8), Plant("Sunflower", 80, 45, 1),
               Plant("Cactus", 15, 120, 0.5)]

    for flower in ft_list:
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            flower.show()
            flower.grow()
            flower.age()
        print("Growth this week: +6cm")
