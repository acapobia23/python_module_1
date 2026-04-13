class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def water_plant(plant_name: str) ->None:
     if plant_name != plant_name.capitalize():
         raise PlantError(f" Invalid plant name to water: {plant_name}")
     print(f"Watering {plant_name}: [OK]")

def test_watering_system():
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrot")

    except PlantError as  e:
        print("Caught PlantError:", e)
    finally:
        print("Closing watering system")

    print()

    print("Testing invalid plants...")
    try:
        water_plant("Tomato")
        water_plant("LEttuce")
        water_plant("CErrot")

    except PlantError as  e:
        print("Caught PlantError:", e)
        return
    finally:
        print("Closing watering system")
        print()
        print("Cleanup always happens, even with errors")
