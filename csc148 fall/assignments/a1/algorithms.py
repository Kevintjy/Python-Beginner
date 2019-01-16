"""CSC148 Assignment 1 - Algorithms

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module Description ===

This file contains two sets of algorithms: ones for generating new arrivals to
the simulation, and ones for making decisions about how elevators should move.

As with other files, you may not change any of the public behaviour (attributes,
methods) given in the starter code, but you can definitely add new attributes
and methods to complete your work here.

See the 'Arrival generation algorithms' and 'Elevator moving algorithsm'
sections of the assignment handout for a complete description of each algorithm
you are expected to implement in this file.
"""
import csv
from enum import Enum
import random
from typing import Dict, List, Optional
from entities import Person, Elevator


###############################################################################
# Arrival generation algorithms
###############################################################################
class ArrivalGenerator:
    """An algorithm for specifying arrivals at each round of the simulation.

    === Attributes ===
    max_floor: The maximum floor number for the building.
               Generated people should not have a starting or target floor
               beyond this floor.
    num_people: The number of people to generate, or None if this is left
                up to the algorithm itself.

    === Representation Invariants ===
    max_floor >= 2
    num_people is None or num_people >= 0
    """
    max_floor: int
    num_people: Optional[int]

    def __init__(self, max_floor: int, num_people: Optional[int]) -> None:
        """Initialize a new ArrivalGenerator.

        Preconditions:
            max_floor >= 2
            num_people is None or num_people >= 0
        """
        self.max_floor = max_floor
        self.num_people = num_people

    def generate(self, round_num: int) -> Dict[int, List[Person]]:
        """Return the new arrivals for the simulation at the given round.

        The returned dictionary maps floor number to the people who
        arrived starting at that floor.

        You can choose whether to include floors where no people arrived.
        """
        raise NotImplementedError


class RandomArrivals(ArrivalGenerator):
    """Generate a fixed number of random people each round.

    Generate 0 people if self.num_people is None.

    For our testing purposes, this class *must* have the same initializer header
    as ArrivalGenerator. So if you choose to to override the initializer, make
    sure to keep the header the same!

    Hint: look up the 'sample' function from random.
    """
    def __init__(self, max_floor: int, num_people: Optional[int]) -> None:
        """Initialize a new ArrivalGenerator.

        Preconditions:
            max_floor >= 2
            num_people is None or num_people >= 0
        """
        super().__init__(max_floor, num_people)

    def generate(self, round_num: int) -> Dict[int, List[Person]]:
        """
        Return the new arrivals for the simulation at the given round.

        The returned dictionary maps floor number to the people who
        arrived starting at that floor.

        """
        if self.num_people is None:
            return {}
        else:
            random_people_dict = {}
            for _i in range(self.num_people):
                start_floor = random.randint(1, self.max_floor)
                target_floor = random.randint(1, self.max_floor)
                while start_floor == target_floor:
                    target_floor = random.randint(1, self.max_floor)
                people = Person(start_floor, target_floor, 0)
                if start_floor not in random_people_dict:
                    random_people_dict[start_floor] = [people]
                else:
                    random_people_dict[start_floor].append(people)
            return random_people_dict


class FileArrivals(ArrivalGenerator):
    """Generate arrivals from a CSV file.

    === Attributes ===

    generator: a dictionary of generated new arrivals, keys and values are
    same as superclass' return value

    """

    generator: dict

    def __init__(self, max_floor: int, filename: str) -> None:
        """Initialize a new FileArrivals algorithm from the given file.

        The num_people attribute of every FileArrivals instance is set to None,
        since the number of arrivals depends on the given file.

        Precondition:
            <filename> refers to a valid CSV file, following the specified
            format and restrictions from the assignment handout.
        """

        ArrivalGenerator.__init__(self, max_floor, None)
        self.generator = {}
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                temp = {}
                i = 1
                while i + 1 < len(line):
                    people = Person(int(line[i]), int(line[i + 1]), 0)
                    if int(line[i].strip()) not in temp:
                        temp[int(line[i].strip())] = [people]
                    else:
                        temp[int(line[i].strip())].extend([people])
                    self.generator[int(line[0].strip())] = temp
                    i += 2

    def generate(self, round_num: int) -> Dict[int, List[Person]]:
        """
        Return the new arrivals for the simulation at the given round.
        The returned dictionary have floor number as keys and people who had
        """
        if round_num in self.generator:
            return self.generator[round_num]
        else:
            return {}


###############################################################################
# Elevator moving algorithms
###############################################################################
class Direction(Enum):
    """
    The following defines the possible directions an elevator can move.
    This is output by the simulation's algorithms.

    The possible values you'll use in your Python code are:
        Direction.UP, Direction.DOWN, Direction.STAY
    """
    UP = 1
    STAY = 0
    DOWN = -1


class MovingAlgorithm:
    """An algorithm to make decisions for moving an elevator at each round.
    """
    def move_elevators(self,
                       elevators: List[Elevator],
                       waiting: Dict[int, List[Person]],
                       max_floor: int) -> List[Direction]:
        """Return a list of directions for each elevator to move to.

        As input, this method receives the list of elevators in the simulation,
        a dictionary mapping floor number to a list of people waiting on
        that floor, and the maximum floor number in the simulation.

        Note that each returned direction should be valid:
            - An elevator at Floor 1 cannot move down.
            - An elevator at the top floor cannot move up.
        """
        raise NotImplementedError


class RandomAlgorithm(MovingAlgorithm):
    """
    A moving algorithm that picks a random direction for each elevator.

    """
    def move_elevators(self,
                       elevators: List[Elevator],
                       waiting: Dict[int, List[Person]],
                       max_floor: int) -> List[Direction]:
        """
        move elevator in  random directions

        """
        direction = [Direction.UP, Direction.STAY, Direction.DOWN]
        result = []
        for elevator in elevators:
            if elevator.current == 1:
                result.append(direction[random.randint(0, 1)])
            elif elevator.current == max_floor:
                result.append(direction[random.randint(1, 2)])
            else:
                result.append(direction[random.randint(0, 2)])
        return result


class PushyPassenger(MovingAlgorithm):
    """A moving algorithm that preferences the first passenger on each elevator.

    If the elevator is empty, it moves towards the *lowest* floor that has at
    least one person waiting, or stays still if there are no people waiting.

    If the elevator isn't empty, it moves towards the target floor of the
    *first* passenger who boarded the elevator.
    """
    def move_elevators(self,
                       elevators: List[Elevator],
                       waiting: Dict[int, List[Person]],
                       max_floor: int) -> List[Direction]:
        """
        Return a list of directions for each elevator to move to.
        if the elevator is empty, move to the lowest floor that has person
        waiting.
        if the elevator is not empty, it moves towards the first passenger's
        target floor.

        """
        def find_small(wait: Dict[int, List[Person]],
                       maximum_floor: int) -> int:
            """
            find the lowest floor number while there is person(s) who waited in
            that floor.
            """
            small = maximum_floor
            temp = []
            for floor, people in wait.items():
                temp += people
                if floor < small and people != []:
                    small = floor
            if len(temp) == 0:
                return 0
            return small

        order = []
        for elevator in elevators:
            if elevator.is_empty():
                direction = find_small(waiting, max_floor)
                if direction == 0:
                    order.append(Direction.STAY)
                elif elevator.current > direction:
                    order.append(Direction.DOWN)
                else:
                    order.append(Direction.UP)
            else:
                if elevator.current < elevator.passengers[0].target:
                    order.append(Direction.UP)
                else:
                    order.append(Direction.DOWN)
        return order


class ShortSighted(MovingAlgorithm):
    """A moving algorithm that preferences the closest possible choice.

    If the elevator is empty, it moves towards the *closest* floor that has at
    least one person waiting, or stays still if there are no people waiting.

    If the elevator isn't empty, it moves towards the closest target floor of
    all passengers who are on the elevator.

    In this case, the order in which people boarded does *not* matter.
    """
    def move_elevators(self,
                       elevators: List[Elevator],
                       waiting: Dict[int, List[Person]],
                       max_floor: int) -> List[Direction]:
        """
        Return a list of directions for each elevator to move to.

        if the elevator is empty, it moves towards to the closest floor that has
        passenger, or stay if no people waiting

        if elevator is not empty, it moves to closest target floor of all
        passengers.

        """
        def find_close_waiting_people(elev: Elevator,
                                      wait: Dict[int, List[Person]]) -> int:
            """
            find the closest floor number that has at least one passenger
            or stay if no people waiting.

            """
            temp4 = []
            is_empty = []
            for floor, people in wait.items():
                is_empty += people
                if len(people) != 0:
                    diff = floor - elev.current
                    temp4.append(diff)
            if len(is_empty) == 0:
                return 0
            temp5 = [abs(item) for item in temp4]
            smaller = min(temp5)
            if -1 * smaller in temp4:
                location = -1 * smaller
            else:
                location = smaller
            return location

        order = []
        for elevator in elevators:
            if elevator.is_empty():
                direction = find_close_waiting_people(elevator,
                                                      waiting)
                if direction > 0:
                    order.append(Direction.UP)
                elif direction == 0:
                    order.append(Direction.STAY)
                else:
                    order.append(Direction.DOWN)
            else:
                temp1 = []
                for passenger in elevator.passengers:
                    temp1.append(passenger.target - elevator.current)
                temp2 = [abs(item) for item in temp1]
                small = min(temp2)
                if -1 * small in temp1:
                    direction = -1 * small
                else:
                    direction = small
                if direction > 0:
                    order.append(Direction.UP)
                else:
                    order.append(Direction.DOWN)
        return order


if __name__ == '__main__':
    # Don't forget to check your work regularly with python_ta!
    # import python_ta
    # python_ta.check_all(config={
    #     'allowed-io': ['__init__'],
    #     'extra-imports': ['entities', 'random', 'csv', 'enum'],
    #     'max-nested-blocks': 4,
    #     'disable': ['R0201']
    # })
    f = FileArrivals(6, "sample_arrivals.csv")
    for i in range(10):
        print(f.generate(i))
