"""CSC148 Lab 5: Linked Lists

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module description ===

This module runs timing experiments to determine how the time taken
to call `len` on a Python list vs. a LinkedList grows as the list size grows.
"""
from timeit import timeit
from linked_list import LinkedList
import matplotlib.pyplot as plt

NUM_TRIALS = 3000                        # The number of trials to run.
SIZES = [1000, 2000, 4000, 8000, 16000]  # The list sizes to try.


def profile_len(list_class: type, size: int) -> float:
    """Return the time taken to call len on a list of the given class and size.

    Precondition: list_class is either list or LinkedList.
    """
    if list_class == list:
        my_list = [i for i in range(size)]
    else:
        my_list = LinkedList([i for i in range(size)])
    time = 0
    time += timeit('len(my_list)', number=1, globals=locals())
    return time


def draw():
    list_temp = []
    linkedlist_temp = []
    for s in SIZES:
        list_temp.append(profile_len(list, s))
        linkedlist_temp.append(profile_len(LinkedList, s))
    plt.plot(SIZES, list_temp)
    plt.annotate('list', xy=(16000, 0.000005))
    plt.plot(SIZES, linkedlist_temp)
    plt.annotate('linked_list', xy=(16000,0.0015))
    plt.xlabel('size')
    plt.ylabel('time')
    plt.show()


if __name__ == '__main__':
    # Try both Python's list and our LinkedList
    # for list_class in [list, LinkedList]:
    #     # Try each list size
    #     for s in SIZES:
    #         time = profile_len(list_class, s)
    #         print(f'[{list_class.__name__}] Size {s:>6}: {time}')
    draw()
