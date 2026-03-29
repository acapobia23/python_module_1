def printday(day: int):
    if (day > 1):
        printday(day - 1)
    print("Day ", day)


def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))
    printday(harvest)
    print("Harvest time!")
