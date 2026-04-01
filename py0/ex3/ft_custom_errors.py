class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def garden_operation(n: int)->None:
    if n == 0:
        raise PlantError
    elif n == 1:
        raise WaterError
    elif n == 2:
        raise GardenError
    else:
        pass

def test_garder() ->None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        garden_operation(0)
    except PlantError as e:
        print("Caught PlantError:", e)
    print()
    print("Testing WaterError...")
    try:
        garden_operation(1)
    except WaterError as e:
        print("Caught WaterError:", e)
    print()
    print("Testing catching all garden errors...")
    try:
        garden_operation(0)
    except GardenError as e:
        print("Caught GardenError:", e)
    try:
        garden_operation(1)
    except GardenError as e:
        print("Caught GardenError:", e)
    print()
    print("All custom error types work correctly!")

test_garder()