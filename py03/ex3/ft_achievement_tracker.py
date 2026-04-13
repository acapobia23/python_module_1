import random

class Player:
    def __init__(self, player: str) -> None:
        self.name = player
        self.acvmts = get_set() # take achievements random



def gen_player_achievements() -> set:
    achievements =  {
                "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
                "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
                "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
                "Boss Slayer"
                }
    player = achievements
    return achievements

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    players = 
    
    print(players)



    # players = {
    #     "Alice" : gen_player_achievements(),
    #     "Bob" : gen_player_achievements(),
    #     "Charlies" : gen_player_achievements(),
    #     "Dylan" : gen_player_achievements()
    # }