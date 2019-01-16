"""CSC148 Assignment 1 - Simulation

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This contains the main Simulation class that is actually responsible for
creating and running the simulation. You'll also find the function `sample_run`
here at the bottom of the file, which you can use as a starting point to run
your simulation on a small configuration.

Note that we have provided a fairly comprehensive list of attributes for
Simulation already. You may add your own *private* attributes, but should not
remove any of the existing attributes.
"""
# You may import more things from these modules (e.g., additional types from
# typing), but you may not import from any other modules.
from typing import Dict, List, Any
import algorithms
from entities import Person, Elevator
from visualizer import Visualizer


class Simulation:
    """The main simulation class.

    === Attributes ===
    arrival_generator: the algorithm used to generate new arrivals.
    elevators: a list of the elevators in the simulation
    moving_algorithm: the algorithm used to decide how to move elevators
    num_floors: the number of floors
    visualizer: the Pygame visualizer used to visualize this simulation
    waiting: a dictionary of people waiting for an elevator
             (keys are floor numbers, values are the list of waiting people)
    wait_time: a list to collect people who completed waiting time
    report: a dictionary that records the data of elevator moving
    """
    arrival_generator: algorithms.ArrivalGenerator
    elevators: List[Elevator]
    moving_algorithm: algorithms.MovingAlgorithm
    num_floors: int
    visualizer: Visualizer
    waiting: Dict[int, List[Person]]
    wait_time: list
    report: dict

    def __init__(self,
                 config: Dict[str, Any]) -> None:
        """Initialize a new simulation using the given configuration."""

        self.arrival_generator = config['arrival_generator']
        self.elevators = [Elevator(config['elevator_capacity'])
                          for _i in range(config['num_elevators'])]
        self.moving_algorithm = config['moving_algorithm']
        self.num_floors = config['num_floors']
        self.visualizer = Visualizer(self.elevators,
                                     self.num_floors,
                                     config['visualize'])
        self.waiting = {}
        self.wait_time = []
        self.report = {
            'num_iterations': 0,
            'total_people': 0,
            'people_completed': 0,
            'max_time': 0,
            'min_time': 0,
            'avg_time': 0
        }

    ############################################################################
    # Handle rounds of simulation.
    ############################################################################
    def run(self, num_rounds: int) -> Dict[str, Any]:
        """Run the simulation for the given number of rounds.

        Return a set of statistics for this simulation run, as specified in the
        assignment handout.

        Precondition: num_rounds >= 1.

        Note: each run of the simulation starts from the same initial state
        (no people, all elevators are empty and start at floor 1).
        """
        for i in range(num_rounds):
            self.visualizer.render_header(i)

            # Stage 1: generate new arrivals
            self._generate_arrivals(i)

            # Stage 2: leave elevators
            self._handle_leaving()

            # Stage 3: board elevators
            self._handle_boarding()

            # Stage 4: move the elevators using the moving algorithm
            self._move_elevators()

            # Pause for 1 second
            self.visualizer.wait(1)

        return self._calculate_stats()

    def _generate_arrivals(self, round_num: int) -> None:
        """Generate and visualize new arrivals."""
        self.report['num_iterations'] += 1
        generate_people = self.arrival_generator.generate(round_num)
        for people in generate_people.values():
            self.report['total_people'] += len(people)
        self.visualizer.show_arrivals(generate_people)
        for floor, people in generate_people.items():
            if floor in self.waiting:
                self.waiting[floor].extend(people)
            else:
                self.waiting[floor] = people
        for elevator in self.elevators:
            for passenger in elevator.passengers:
                passenger.wait_time += 1

    def _handle_leaving(self) -> None:
        """Handle people leaving elevators."""
        for elevator in self.elevators:
            for passenger in elevator.passengers:
                if elevator.current == passenger.target:
                    elevator.passengers.remove(passenger)
                    self.report['people_completed'] += 1
                    self.wait_time.append(passenger.wait_time)
                    self.report["max_time"] = max(self.wait_time)
                    self.report['min_time'] = min(self.wait_time)
                    self.report['avg_time'] = sum(self.wait_time) //\
                                              len(self.wait_time)
                    self.visualizer.show_disembarking(passenger, elevator)

    def _handle_boarding(self) -> None:
        """Handle boarding of people and visualize."""
        for elevator in self.elevators:
            if elevator.current in self.waiting:
                people = self.waiting[elevator.current][:]
            else:
                people = []
            for person in people:
                if elevator.fullness() < 1.0:
                    self.waiting[elevator.current].remove(person)
                    elevator.passengers.append(person)
                    self.visualizer.show_boarding(person, elevator)

    def _move_elevators(self) -> None:
        """Move the elevators in this simulation.

        Use this simulation's moving algorithm to move the elevators.
        """
        order = self.moving_algorithm.move_elevators(self.elevators,
                                                     self.waiting,
                                                     self.num_floors)
        self.visualizer.show_elevator_moves(self.elevators, order)
        for i in range(len(order)):
            self.elevators[i].current += order[i].value
        for human in self.waiting.values():
            for person in human:
                person.wait_time += 1


    ############################################################################
    # Statistics calculations
    ############################################################################
    def _calculate_stats(self) -> dict:
        """Report the statistics for the current run of this simulation.
        """
        if self.report['people_completed'] == 0:
            self.report['min_time'] = -1
            self.report['max_time'] = -1
            self.report['avg_time'] = -1
        return self.report


def sample_run() -> Dict[str, int]:
    """Run a sample simulation, and return the simulation statistics."""
    config = {
        'num_floors': 6,
        'num_elevators': 6,
        'elevator_capacity': 3,
        'num_people_per_round': 2,
        # Random arrival generator with 6 max floors and 2 arrivals per round.
        'arrival_generator': algorithms.FileArrivals(6, "sample_arrivals.csv"),
        'moving_algorithm': algorithms.RandomAlgorithm(),
        'visualize': True
    }

    sim = Simulation(config)
    stats = sim.run(15)
    return stats


if __name__ == '__main__':
    # Uncomment this line to run our sample simulation (and print the
    # statistics generated by the simulation).
    print(sample_run())
    #
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['entities', 'visualizer', 'algorithms', 'time'],
    #     'max-nested-blocks': 4})
