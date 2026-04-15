class Plant:
    def __init__(self, name: str, height: float, old: int,
                 rate: float = 1) -> None:
        self.name = name
        if self.set_height(height, False) is False:
            self.__height = 0.0
        if self.set_old(old, False) is False:
            self.__old = 0
        self.rate = round(rate, 2)

    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self.__height = round(self.get_height() + self.rate, 2)

    def age(self) -> None:
        self.__old = round(self.get_age() + 1)

    def set_height(self, height: float, verbose: bool = True) -> bool:
        if height < 0:
            if verbose is True:
                print(f"{self.name}:  Error, height can't be negative")
                print("Height update rejected")
            return False
        else:
            self.__height = round(height, 2)
            if verbose is True:
                print(f"Height updated: {height}")
            return True

    def set_old(self, old: int, verbose: bool = True) -> bool:
        if old < 0:
            if verbose is True:
                print(f"{self.name}:  Error, age can't be negative")
                print("Age update rejected")
            return False
        else:
            self.__old = round(old)
            if verbose is True:
                print(f"old updated: {old} days")
            return True

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__old


class Flower(Plant):
    def __init__(self, name: str, height: float, old: int, color: str,
                 rate: float = 1) -> None:
        super().__init__(name, height, old)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.bloomed:
            print(" Rose has not bloomed yet")
        else:
            print(" Rose is blooming beautifully!")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, old: int,
                 trunk_diameter: float, rate: float = 1) -> None:
        super().__init__(name, height, old)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self.get_height()}"
              f"cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, old: int,
                 harvest_season: str, nutritional_value: int,
                 rate: float = 1) -> None:
        super().__init__(name, height, old, rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0, 2.1)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(0, 20):
        tomato.grow()
        tomato.age()
        i += 1
    tomato.show()
