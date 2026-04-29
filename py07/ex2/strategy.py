from abc import ABC, abstractmethod
from ex0.creature import Creature

class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:        
        return True

class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:        
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception("Invalid Creature "
                  f"'{creature.name}' for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:        
        return hasattr(creature, "heal")

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception("Invalid Creature "
                  f"'{creature.name}' for this defensive strategy")
        print(creature.attack())
        print(creature.heal())
    