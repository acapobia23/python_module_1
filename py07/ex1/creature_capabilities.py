from abc import ABC, abstractmethod
from ex0.creature import Creature

class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Creature) -> str:
        pass

class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed = False
    
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")
        HealCapability.__init__(self)
    
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"
    
    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals {target.name} or a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"
    
    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self.name} heals itself and others for a large amount"
        else:
            return f"{self.name} heals {target.name} and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"
    
    def transform(self) -> str:
        if self.is_transformed is True:
            return f"{self.name} is already transformed"
        else:
            self.is_transformed = True
            return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        if self.is_transformed is False:
            return f"{self.name} is already reverted"
        else:
            self.is_transformed = False
            return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"
    
    def transform(self) -> str:
        if self.is_transformed is True:
            return f"{self.name} is already transformed"
        else:
            self.is_transformed = True
            return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if self.is_transformed is False:
            return f"{self.name} is already reverted"
        else:
            self.is_transformed = False
            return f"{self.name} stabilizes its form."