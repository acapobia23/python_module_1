class Plant:
    def __init__(self, name: str, height: float, old: int, rate: float = 1) -> None:
        self.name = name
        if (self.set_height(height, False) == False):
            self.__height = 0
        if (self.set_old(old, False) == False):
            self.__old = 0
        self.rate = round(rate, 2)
        self.info = self.Stats()

    class Stats:
        def __init__(self) -> None:
            self.__c_grow = 0
            self.__c_age = 0
            self.__c_show = 0
        
        def get_c_grow(self) -> int:
            return self.__c_grow

        def set_c_grow(self) -> None:
            self.__c_grow = self.get_c_grow() + 1

        def get_c_age(self) -> int:
            return self.__c_age

        def set_c_age(self) -> None:
            self.__c_age = self.get_c_age() + 1

        def get_c_show(self) -> int:
            return self.__c_show

        def set_c_show(self) -> None:
            self.__c_show = self.get_c_show() + 1

    @staticmethod
    def check_age(days: int) -> None:
        if (days > 365):
            print(f"Is {days} days more than a year? -> True")
        else:
            print(f"Is {days} days more than a year? -> False")

    @classmethod
    def unknow(cls) -> None:
        return cls("Unknown plant", 0.0, 0)
    
    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self.__height = round(self.get_height() + self.rate, 2)

    def age(self) -> None:
        self.__old = round(self.get_age() + 1)
    
    def set_height(self, height: float, verbose: bool = True) ->bool:
        if (height < 0):
            if verbose == True:
                print(f"{self.name}:  Error, height can't be negative")
                print("Height update rejected")
            return False
        else:
            self.__height = round(height, 2)
            if verbose == True:
                print(f"Height updated: {height}")
            return True

    def set_old(self, old: int, verbose: bool = True) ->bool:
        if (old < 0):
            if verbose == True:
                print(f"{self.name}:  Error, age can't be negative")
                print("Age update rejected")
            return False
        else:
            self.__old = round(old)
            if verbose == True:
                print(f"old updated: {old} days")
            return True

    def get_height(self) ->float:
        return self.__height
    
    def get_age(self) -> int:
        return self.__old


class Flower(Plant):
    def __init__(self, name: str, height: float, old: int, color: str,\
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

class Seed(Flower):
    def __init__(self, name: str, height: float, old: int, color: str,\
                    seed: float, rate: float = 1) -> None:
        super().__init__(name, height, old, color, rate)
        self.seed = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed += 42

    def show(self) -> None:
        super().show()
        print(f" Seed: {self.seed}")



class Tree(Plant):
    def __init__(self, name: str, height: float, old: int,  trunk_diameter: float,\
                     rate: float = 1) -> None:
        super().__init__(name, height, old)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
    
    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self.get_height()}cm long and {self.trunk_diameter}cm wide.")

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            self.__c_shade = 0

        def get_c_shade(self) -> int:
            return self.__c_shade

        def set_c_shade(self) -> None:
            self.__c_shade = self.get_c_shade() + 1

class Vegetable(Plant):
    def __init__(self, name: str, height: float, old: int,   harvest_season: str,\
                     nutritional_value: int, rate: float = 1) -> None:
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


def show_stats(stat:) -> None:


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0, 1.5)
    unknow_plant = Plant.unknow()

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
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for i in range(0, 20):
        sunflower.grow()
        sunflower.age()
        i += 1
    sunflower.bloom()
    sunflower.show()
    print()
    print("=== Anonymous")
    unknow_plant.show()