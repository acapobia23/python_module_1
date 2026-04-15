import random


if __name__ == "__main__":
    names = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
             "john", "kevin", "Liam"]
    first = [name.capitalize() for name in names]
    second = [name for name in names if name.istitle()]

    print("=== Game Data Alchemist ===")
    print()
    print("Initial list of players:", names)
    print("New list with all names capitalized:", first)
    print("New list of capitalized names only:", second)
    print()
    players = {name: random.randrange(0, 999) for name in names}
    average = round((sum(players.values()) / len(players)), 2)
    score = {key: value for key, value in players.items() if value > average}
    print("Score dict:", players)
    print("Score average is ", average)
    print("High scores:", score)
