def ft_count_harvest_iterative():
    harvest = int(input("Days until harvest: "))
    x = range(harvest)
    for n in x:
        print("Day", n + 1)
    print("Harvest time!")
