import random


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements = set()

    def show(self) -> None:
        print(f"player {self.name}: {self.achievements}")


def get_list() -> list:
        all_acvm = [ 'Crafting Genius', 'Strategist', 'World Savior',
        'Master Explorer', 'Collector Supreme', 'Untouchable',
        'Boss Slayer', 'Unstoppable', 'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
        ]
        return all_acvm


def get_set() -> set:
        all_acvm = [ 'Crafting Genius', 'Strategist', 'World Savior',
        'Master Explorer', 'Collector Supreme', 'Untouchable',
        'Boss Slayer', 'Unstoppable', 'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
        ]
        return set(all_acvm)

def gen_player_achievements() -> set:

    all_acvm = get_list()
    count_add = random.randint(1, 14)
    return set(random.sample(all_acvm, count_add))

def show_all_achievements(players:list) -> None:
    all_acvm = set()
    i = 0

    while i < len(players):
        all_acvm = all_acvm.union(players[i].achievements)
        i += 1
    print("All distinct achievements:", all_acvm)

def show_common_achievements(players) ->None:
    length = len(players)

    if length == 0:
         return
    elif length == 1:
        print("Common achievements:", players[0].achievements)
        return
    common = players[0].achievements.intersection(players[1].achievements)
    i = 2
    while i < length:
         common = common.intersection(players[i].achievements)
         i += 1
    print("Common achievements:", common)


def show_only_achievements(players: list) -> None:
    i = 0

    while i < len(players):
        y = 0
        acvmt_all = set()
        only = set()
        while y < len(players):
            if y != i:
                acvmt_all = acvmt_all.union(players[y].achievements)
            y += 1
        only = players[i].achievements.difference(acvmt_all)
        print("Only", players[i].name ,"has :", only)
        i += 1


def show_missing_achievements(players: list) -> None:
    length = len(players)
    i = 0
    all_acvm = get_set()
    while i < length:
        missing = all_acvm.difference(players[i].achievements)
        print(players[i].name, "is missing:", missing)
        i += 1

if __name__ == "__main__":
    players = [Player("Alice"), Player("Bob"),
        Player("Charlies"), Player("Dylan")
    ]

    print("=== Achievement Tracker System ===\n")
    i = 0
    
    while i < len(players):
        players[i].achievements = gen_player_achievements()
        players[i].show()
        i += 1
    print()
    show_all_achievements(players)
    print()
    show_common_achievements(players)
    print()
    show_only_achievements(players)
    print()
    show_missing_achievements(players)
    print()