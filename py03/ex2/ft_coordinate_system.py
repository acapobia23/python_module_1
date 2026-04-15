import math

class CordinateError(Exception):
    def __init__(self, message="Unknow cordinate error"):
        super().__init__(message)


class CordinateInputError(CordinateError):
    def __init__(self, message="Invalid syntax"):
        super().__init__(message)


def get_player_pos() -> tuple:
    numbers = ()
    flag = 0
    mtx = []

    while flag == 0:
        try:
            str = input("Enter new coordinates as floats in format 'x,y,z': ")
            str = str.replace(",", " ")
            mtx = str.split()
            i = 0
            while True:
                try:
                    mtx[i]
                    i += 1
                except:
                    break
            if i != 3:
                raise CordinateInputError
            i = 0
            while i < 3:
                numbers = numbers + (round(float(mtx[i]), 1),)
                i += 1                        
            flag = 1
        except CordinateInputError as e:
            print(e)
        except ValueError as e:
            print(f"Error on parameter '{mtx[i]}': {e}")
    return numbers

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    first = get_player_pos()
    print("Get a first set of coordinates")
    print("Got a first tuple:", first)
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    distance =  round(math.sqrt((0 - first[0])**2 + (0 - first[1])**2 + (0- first[2])**2), 4)
    print("Distance to center:", distance)
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    distance = round(math.sqrt(( second[0] - first[0])**2 + (first[1])**2 + (second[2] - first[2])**2), 4)
    print("Distance to center:", distance)
    print()
