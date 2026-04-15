import sys


class InventoryError(Exception):
    def __init__(self, message="Unknow Error"):
        super().__init__(message)


class InventoryValueError(InventoryError):
    def __init__(self, item: str):
        super().__init__(f"Error - invalid parameter '{item}'")


class InventoryRedundantError(InventoryError):
    def __init__(self, item: str):
        super().__init__(f"Redundant item '{item}' - discarding")


def get_item(arg: str) -> list:
    item = []

    if arg.count(":") == 0:
        raise InventoryValueError(arg)
    else:
        item = list(arg.split(":"))
    return item


def inventory_dict() -> dict:
    inv = {}
    i = 1

    if len(sys.argv) == 1:
        return inv

    while i < len(sys.argv):
        try:
            item = get_item(sys.argv[i])
            if item[0] in inv:
                raise InventoryRedundantError(item[0])
            item[1] = int(item[1])
            inv.update({item[0]: item[1]})
        except InventoryRedundantError as e:
            print(e)
        except InventoryValueError as e:
            print(e)
        except ValueError as e:
            print(f"Quantity error for '{item[0]}': {e}")
        i += 1
    return inv


def show_percents(inventory: dict) -> None:
    total = sum(inventory.values())
    values = list(inventory.keys())
    i = 0
    while i < len(values):
        tmp = float(inventory[values[i]])
        percent = round(((tmp * 100) / total), 2)
        print(f"Item {values[i]} represents {percent}%")
        i += 1


def show_min_max(inventory: dict) -> None:
    values = list(inventory.values())
    key = list(inventory.keys())
    mininum = min(values)
    maximun = max(values)
    i = 0
    while i < len(key):
        if values[i] == maximun:
            print(f"Item most abundant: {key[i]} with quantity {values[i]}")
            break
        else:
            i += 1
    i = 0
    while i < len(key):
        if values[i] == mininum:
            print(f"Item least abundant: {key[i]} with quantity {values[i]}")
            break
        i += 1


if __name__ == "__main__":
    inventory = {}

    print("=== Inventory System Analysis ===")
    inventory = inventory_dict()
    print("Got inventory :", inventory)
    print("Item list:", inventory.keys())
    print("Total quantity of the", len(inventory.keys()), "items:",
          sum(inventory.values()))
    show_percents(inventory)
    show_min_max(inventory)
    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)
