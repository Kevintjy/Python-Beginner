"""CSC148 Lab 1

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains a function that searches for an item in a list,
and illustrates how to use doctest.
"""
from typing import Any


def binary_search(x, lst,low = 0, high = None) -> int:
    """Return the index of <t> in <lst>, or -1 if it does not occur.

    Preconditions:
    - L is sorted.
      Specifically, lst[0] <= lst[1] ... <= lst[n-1], where n is len(lst).
    - t can be compared to the elements of lst.

    >>> binary_search(11, [2, 4, 7, 8, 11])
    4
    >>> binary_search(5, [2, 4, 7, 8, 11])
    -1
    >>> binary_search(5, [0, 5, 10, 15, 20, 25, 30, 35, 40])
    1

    """
    if high is None:
        high = len(lst)
    while low < high:
        mid = low + (high - low)//2
        if x == lst[mid]:
            return mid
        if x < lst[mid]:
            return binary_search(x,lst,low,mid)
        else:
            return binary_search(x,lst,mid+1,high)
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()