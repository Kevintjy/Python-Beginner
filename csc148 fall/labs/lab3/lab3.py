"""CSC148 Lab 3: Inheritance

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the implementation of a simple number game.
The key class design feature here is *inheritance*, which is used to enable
different types of players, both human and computer, for the game.
"""
from __future__ import annotations
import random
from typing import Tuple


class NumberGame:
    """A number game for two players.

    A count starts at 0. On a player's turn, they add to the count an amount
    between a set minimum and a set maximum. The player who brings the count
    to a set goal amount is the winner.

    The game can have multiple rounds.

    === Attributes ===
    goal:
        The amount to reach in order to win the game.
    min_step:
        The minimum legal move.
    max_step:
        The maximum legal move.
    current:
        The current value of the game count.
    players:
        The two players.
    turn:
        The turn the game is on, beginning with turn 0.
        If turn is even number, it is players[0]'s turn.
        If turn is any odd number, it is player[1]'s turn.

    === Representation invariants ==
    - self.turn >= 0
    - 0 <= self.current <= self.goal
    - 0 < self.min_step <= self.max_step <= self.goal
    """
    goal: int
    min_step: int
    max_step: int
    current: int
    players: Tuple[Player, Player]
    turn: int

    def __init__(self, goal: int, min_step: int, max_step: int,
                 players: Tuple[Player, Player]) -> None:
        """Initialize this NumberGame.

        Preconditions:
            0 < min_step <= max_step <= goal
        """
        self.goal = goal
        self.min_step = min_step
        self.max_step = max_step
        self.current = 0
        self.players = players
        self.turn = 0

    def play(self) -> str:
        """Play one round of this NumberGame. Return the name of the winner.

        A "round" is one full run of the game, from when the count starts
        at 0 until the goal is reached.
        """
        while self.current < self.goal:
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        winner = self.whose_turn(self.turn - 1)
        winner.report += 1
        return winner.name

    def whose_turn(self, turn: int) -> Player:
        """Return the Player whose turn it is on the given turn number.
        """
        if turn % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]

    def play_one_turn(self) -> None:
        """Play a single turn in this NumberGame.

        Determine whose move it is, get their move, and update the current
        total as well as the number of the turn we are on.
        Print the move and the new total.
        """
        next_player = self.whose_turn(self.turn)
        amount = next_player.move(
            self.current,
            self.min_step,
            self.max_step,
            self.goal
        )
        self.current += amount
        self.turn += 1

        print(f'{next_player.name} moves {amount}.')
        print(f'Total is now {self.current}.')

class Player:
    """
    an abstract class to describe the class of player

    === Attributes ===
    name: the name of the player.
    """
    name: str
    report: int

    def __init__(self, name: str) -> None:
        self.name = name
        self.report = 0

    def move(self, current: int, minimum: int, maximum: int, goal: int) -> int:
        """
        return an int to show how many steps it move
        """
        raise NotImplementedError

    def __str__(self) -> str:
        return '{} wins {} times'.format(self.name, self.report)


class RandomPlayer(Player):
    """
    the subclass of Player
    """
    def move(self, current: int, minimum: int, maximum: int, goal: int) -> int:
        """
        move randomly
        """
        return random.randint(minimum, maximum)


class UserPlayer(Player):
    """
    the subclass of Player
    """
    def move(self, current: int, minimum: int, maximum: int, goal: int) -> int:
        """
        move by the input
        """
        step = input("please input your step: \n")
        temp = [x for x in range(minimum, maximum + 1)]
        while step not in temp:
            print(step)
            print("your input is not in the range")
            self.move(current, minimum, maximum, goal)
        return int(step)


class StrategicPlayer(Player):
    """
    the subclass of Player
    """
    def move(self, current: int, minimum: int, maximum: int, goal: int) -> int:
        """
        move by the best choose
        """
        if current == 0:
            return goal % (maximum + minimum) if goal % (maximum + minimum) >= minimum else random.randint(minimum, maximum)
        step = (goal - current) % (maximum + minimum)
        return step if step >= minimum else random.randint(minimum, maximum)


def make_player(generic_name: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.
    """
    name = input(f'Enter a name for {generic_name}: ')
    if generic_name == "RandomPlayer":
        return RandomPlayer(name)
    if generic_name == "UserPlayer":
        return UserPlayer(name)
    if generic_name == "StrategicPlayer":
        return StrategicPlayer(name)
    else:
        print('generic_name not found')
        generic_name = input('please input your new generic_name')
        make_player(generic_name)


def main() -> None:
    """Play multiple rounds of a NumberGame based on user input settings.
    """
    goal = int(input('Enter goal amount: '))
    minimum = int(input('Enter minimum move: '))
    maximum = int(input('Enter maximum move: '))
    p1 = make_player('StrategicPlayer')
    p2 = make_player('UserPlayer')
    while True:
        g = NumberGame(goal, minimum, maximum, (p1, p2))
        winner = g.play()
        print(f'And {winner} is the winner!!!')
        print(p1)
        print(p2)
        again = input('Again? (y/n) ')
        if again != 'y':
            return


if __name__ == '__main__':
    # Uncomment the lines below to check your work using
    #python_ta and doctest.
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['random'],
    #     'allowed-io': [
    #         'main',
    #         'make_player',
    #         'move',
    #         'play_one_turn'
    #     ]
    # })
    # import doctest
    # doctest.testmod()

    # Uncomment the following line to run the number game.
    main()
