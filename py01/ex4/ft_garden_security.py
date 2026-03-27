class Plant:
    def __init__(self, name: str, height: float, old: int, rate: float = 1) -> None:
        self.name = name
        if (self.set_height(height, False) == False):
            self.__height = 0
        if (self.set_old(old, False) == False):
            self.__old = 0
        self.rate = round(rate, 2)

    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    def grow(self) -> None:
        self.__height = round(self.__height + self.rate, 2)

    def age(self) -> None:
        self.__old += 1
    
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


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_old(30)
    print()
    rose.set_height(-5.15)
    rose.set_old(-9.99)
    print()
    print("Current state:", end=" ")
    rose.show()
