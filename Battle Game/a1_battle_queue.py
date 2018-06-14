"""
The BattleQueue class for A1.

A BattleQueue is a queue that lets our game know in what order various 
characters are going to attack. The method headers and descriptions have all 
been provided for you, but the implementation will depend on you.

You must replace the 'Any's in the type annotations as well as add in
the constructors for the docstring examples.
"""
# TODO: In the type annotations, replace Any with the appropriate types.
# To put a class name without importing it, just wrap the name in ''s.
# For example:
# add(self, character: 'Something') -> None:
#
# If there are multiple return types, import Union and use that. For example:
# Union[str, bool]
from typing import Any
from a1_character import Character, Rogue, Mage
from typing import Union

class BattleQueue:
    """
    A class representing a BattleQueue.
    """
    
    def __init__(self):
        """
        Initialize this BattleQueue.
        
        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        """
        self.characters = []
    
    def add(self, character: Character) -> None:
        """
        Add character to this BattleQueue.
        
        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import Rogue
        >>> c = Rogue('Sophia', BattleQueue, ps)
        >>> bq.add(c)
        >>> bq.is_empty()
        False
        """
        self.characters.append(character)
    
    def remove(self) -> Character():
        """
        Remove and return the character at the front of this BattleQueue.
        
        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import Rogue
        >>> c = Rogue('Sophia', BattleQueue, ps)
        >>> bq.add(c)
        >>> bq.remove()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        True
        """
        if not self.is_empty():
            temp = self.characters[0]
            self.characters.pop(0)
            return temp
    
    def is_empty(self) -> bool:
        """
        Return whether this BattleQueue is empty (i.e. has no players or
        has no players that can perform any actions).
        
        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        """
        if len(self.characters) == 0:
            return True
        flag = False
        for i in self.characters:
            if i.get_available_actions == []:
                flag = True
        return flag
    
    def peek(self) -> Character():
        """
        Return the character at the front of this BattleQueue but does not
        remove them.
        
        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import Rogue
        >>> c = Rogue('Sophia', BattleQueue, ps)
        >>> bq.add(c)
        >>> bq.peek()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        False
        """
        if not self.is_empty():
            return self.characters[0]
    
    def is_over(self) -> bool:
        """
        Return whether the game being carried out in this BattleQueue is over 
        or not.
        
        A game is considered over if:
            - Both players have no skills that they can use.
            - One player has 0 HP
            or
            - The BattleQueue is empty.
            
        >>> bq = BattleQueue()
        >>> bq.is_over()
        True
        
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_character import Rogue
        >>> c = Rogue('Sophia', BattleQueue, ps)
        >>> bq.add(c)
        >>> bq.is_over()
        False
        """
        if self.is_empty():
            return True
        if self.characters[0].HP == 0 or self.characters[1].HP == 0:
            return True
        return (self.characters[0].get_available_actions() == [] and
                self.characters[1].get_available_actions() == [])

    def get_winner(self) -> Union[None, Character]:
        """
        Return the winner of the game being carried out in this BattleQueue
        if the game is over. If the game is not over or if there is no winner
        (i.e. there's a tie), return None.
        
        >>> bq = BattleQueue()
        >>> bq.get_winner()
        """
        if self.is_over():
            for i in self.characters:
                if i.HP < 0:
                    del i
        if len(self.characters) > 0:
            for j in self.characters:
                return j
        return None

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
