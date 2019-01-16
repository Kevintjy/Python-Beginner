"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module runs timing experiments to determine how the time taken
to enqueue or dequeue grows as the queue size grows.
"""
from timeit import timeit
from typing import List, Tuple
import matplotlib.pyplot as plt
from myqueue import Queue


###############################################################################
# Task 3: Running timing experiments
###############################################################################
# TODO: implement this function
def _setup_queues(qsize: int, n: int) -> List[Queue]:
    """Return a list of <n> queues, each of the given size."""
    # Experiment preparation: make a list containing <n> queues,
    # each of size <qsize>.
    # You can "cheat" here and set your queue's _items attribute directly
    # to a list of the appropriate size by writing something like
    #
    #     queue._items = list(range(qsize))
    #
    # to save a bit of time in setting up the experiment.

    result = []
    for _i in range(n):
        q = Queue()
        q._item = list(range(qsize))
        result.append(q)
    return result



def time_queue() -> None:
    """Run timing experiments for Queue.enqueue and Queue.dequeue."""
    # The queue sizes to try.
    queue_sizes = [10000, 20000, 40000, 80000, 160000]

    # The number of times to call a single enqueue or dequeue operation.
    trials = 200

    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.enqueue(1)', number=1, globals=locals())
        print(f'enqueue: Queue size {queue_size:>7}, time {time}')

    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.dequeue()', number=1, globals=locals())
        print(f'dequeue: Queue size {queue_size:>7}, time {time}')

def time_queue_lists() -> Tuple[List[int], List[float], List[float]]:
    """Run timing experiments for Queue.enqueue and Queue.dequeue.

    Return lists storing the results of the experiments.
    """
    queue_sizes = [10000, 20000, 40000, 80000, 160000]
    trials = 200
    temp1 = []
    temp2 = []
    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.enqueue(1)', number=1, globals=locals())
        temp1.append(time)
    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.dequeue()', number=1, globals=locals())
        temp2.append(time)
    return queue_sizes, temp1, temp2


def draw_enqueue() -> None:
    """draw the enqueue graph"""
    data = time_queue_lists()
    plt.plot(data[0], data[1])
    plt.axis([0, 40000, 0, 0.005])
    plt.xlabel("queue size")
    plt.ylabel('time')
    plt.show()


def draw_dequeue() -> None:
    """draw the enqueue graph"""
    data = time_queue_lists()
    plt.plot(data[0], data[2])
    plt.axis([0, 40000, 0, 0.005])
    plt.xlabel("queue size")
    plt.ylabel('time')
    plt.show()



if __name__ == '__main__':
    draw_dequeue()



