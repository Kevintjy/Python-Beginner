"""
Lab 3 solutions. This contains:
    - The solution to the warm-up problem
    - Solution to list_container
    - Solution to list_nestedness
    - Implementation of StackQueue

Solution to the warm-up problem:
    Step                   Queue                      Items removed
    1. Add "E"             Front -> E
    2. Add "S"             Front -> E, S
    3. Remove an item      Front -> S                 E
    4. Add "U"             Front -> S, U              E
    5. Add "E"             Front -> S, U, E           E
    6. Add "A"             Front -> S, U, E, A        E
    7. Add "T"             Front -> S, U, E, A, T     E
    8. Remove an item      Front -> U, E, A, T        E, S
    9. Remove an item      Front -> E, A, T           E, S, U
    10. Add "U"            Front -> E, A, T, U        E, S, U
    11. Add "K"            Front -> E, A, T, U, K     E, S, U
    12. Add "C"            Front -> E, A, T, U, K, C  E, S, U
    13. Remove an item     Front -> A, T, U, K, C     E, S, U, E
    14. Remove an item     Front -> T, U, K, C        E, S, U, E, A
    15. Add "Q"            Front -> T, U, K, C, Q     E, S, U, E, A
    16. Keep removing items until it's empty          ...
                                                      E, S, U, E, A, T, U, K, C,
                                                      Q

    Step                   Stack                      Items removed
    1. Add "E"             Top -> E
    2. Add "S"             Top -> S, E
    3. Remove an item      Top -> E                 S
    4. Add "U"             Top -> U, E              S
    5. Add "E"             Top -> E, U, E           S
    6. Add "A"             Top -> A, E, U, E        S
    7. Add "T"             Top -> T, A, E, U, E     S
    8. Remove an item      Top -> A, E, U, E        S, T
    9. Remove an item      Top -> E, U, E           S, T, A
    10. Add "U"            Top -> U, E, U, E        S, T, A
    11. Add "K"            Top -> K, U, E, U, E     S, T, Aa
    12. Add "C"            Top -> C, K, U, E, U, E  S, T, A
    13. Remove an item     Top -> K, U, E, U, E     S, T, A, C
    14. Remove an item     Top -> U, E, U, E        S, T, A, C, K
    15. Add "Q"            Top -> Q, U, E, U, E     S, T, A, C, K
    16. Keep removing items until it's empty        ...
                                                    S, T, A, C, K, Q, U, E, U, E


Note: This file has 1 PythonTA error (too many nested blocks). That's fine.
      It's necessary for list_nestedness.
"""
from typing import List
from adts import Container, Queue, Stack


def list_container(lst: List[int], c: Container) -> None:
    """
    Empty out c according to the algorithm from lecture after filling it with
    items from lst.

    When c is a Stack, the elements of lst should be printed in reverse order.
    When c is a Queue, the elements of lst should be printed out in level order.

    Precondition: c is empty.

    >>> lst = [1, [[[2], 3]], [4, [5]]]
    >>> list_container(lst, Stack())
    5
    4
    3
    2
    1
    >>> list_container(lst, Queue())
    1
    4
    3
    5
    2
    """
    # Step 1. Add all of the items from lst into c
    for item in lst:
        c.add(item)

    # Step 2. Repeat the following until c is empty
    while not c.is_empty():
        # Step 2a. Remove an item from the container
        removed_item = c.remove()

        # Step 2b. If that item is not a list, print it out
        if not isinstance(removed_item, list):
            print(removed_item)
        else:
            # Step 2c. If it is a list, add all of its items into c
            for item in removed_item:
                c.add(item)


def list_nestedness(lst: List[int], q: Queue) -> List[List[int]]:
    """
    Return a list of elements of lst in each level of nestedness using q.

    Precondition: q is empty.
                  lst contains only ints.

    >>> lst = [1, [[[2], 3]], [4, [5]]]
    >>> list_nestedness(lst, Queue())
    [[1], [4], [3, 5], [2]]
    """
    # Step 1. Add all of the items from lst into c
    for item in lst:
        q.add(item)

    # LIST_NESTEDNESS - 2. Add "END" to the Queue
    q.add("END")

    # LIST_NESTEDNESS - 3. Create an empty list called level
    level = []

    # LIST_NESTEDNESS - 4. Create an empty list called all_levels
    all_levels = []

    # Step 2. Repeat the following until c is empty
    while not q.is_empty():
        # Step 2a. Remove an item from the container
        removed_item = q.remove()

        # Step 2b. If that item is not a list, print it out
        if not isinstance(removed_item, list):
            # LIST_NESTEDNESS - 5B. If removed_item is "END" append level to
            # all_levels and set level to an empty list.
            if removed_item == "END":
                all_levels.append(level)
                level = []

                # LIST_NESTEDNESS - 5BI. If the Queue is not empty, add "END"
                # to the Queue
                if not q.is_empty():
                    q.add("END")
            else:
                # LIST_NESTEDNESS - 5C. If removed_item is not a list or "END",
                # add it to the list 'level'
                level.append(removed_item)
        else:
            # Step 2c. If it is a list, add all of its items into c
            for item in removed_item:
                q.add(item)

    # Return all_levels when we're done.
    return all_levels


class StackQueue(Container):
    """
    An implementation of the class Queue but using Stacks to store the
    content.
    """

    def __init__(self) -> None:
        """
        Initialize this StackQueue.

        >>> q = StackQueue()
        >>> q.is_empty()
        True
        """
        # Create 2 stacks as attributes
        # self._add_to: This will be the stack that we always add to when
        #               add() is called.
        # self._remove_from: This will be the stack that we use to remove from
        #               when remove() is called.
        self._add_to = Stack()
        self._remove_from = Stack()

    def add(self, value: object) -> None:
        """
        Add value to this StackQueue.

        >>> q = StackQueue()
        >>> q.add(5)
        >>> q.add(3)
        >>> q.remove()
        5
        >>> q.remove()
        3
        """
        # Simply add to self._add_to for add()
        self._add_to.add(value)

    def remove(self) -> object:
        """
        Remove the item at the front of this StackQueue.

        >>> q = StackQueue()
        >>> q.add(5)
        >>> q.add(3)
        >>> q.remove()
        5
        >>> q.remove()
        3
        """
        # Empty out self._add_to and put all of the items into self._remove_from
        # In this case, you'll be adding the items in reverse order.
        # If self._add_to looked like Top -> 4, 3, 2, 1
        # Then removing from it would give Top -> 3, 2, 1
        # Adding that to self._remove_from would make it Top -> 4
        # Removing the next item from self._add_to would make it Top -> 2, 1
        # And adding that to self._remove_from would make it Top -> 3, 4
        # So by the time self._add_to is empty, self._remove will have the
        # items in reverse order.

        # Empty our self._add_to
        while not self._add_to.is_empty():
            # Add the item removed into self._remove_from
            self._remove_from.add(self._add_to.remove())

        # We remove from self._remove_from to get the 'first item' in our Queue
        return_value = self._remove_from.remove()

        # And then we put self._add_to back in its original order sans that
        # first item (e.g. empty our self._remove_from into self._add_to)

        # Empty our self._remove_from
        while not self._add_to.is_empty():
            # Add the item removed into self._add_to
            self._add_to.add(self._remove_from.remove())

        return return_value

    def is_empty(self) -> bool:
        """
        Return whether this StackQueue is empty or not.

        >>> q = StackQueue()
        >>> q.is_empty()
        True
        >>> q.add(5)
        >>> q.is_empty()
        False
        """
        # Since we always add to self._add_to, we just return whether that's
        # empty or not
        return self._add_to.is_empty()


if __name__ == '__main__':


    import doctest

    doctest.testmod()
