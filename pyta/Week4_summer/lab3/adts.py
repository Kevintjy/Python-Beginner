"""
The ADTs implemented from lecture.

This includes the Stack, Queue, and an abstract parent class (Container)

REMINDER: NEVER USE THE NAME stack.py OR queue.py FOR YOUR FILES.
          PythonTA will break. :(
"""


class Container:
    """
    An abstract Container class.
    """

    def __init__(self) -> None:
        """
        Initialize this Container.
        """
        raise NotImplementedError

    def add(self, value) -> None:
        """
        Add value this Container.
        """
        raise NotImplementedError

    def remove(self) -> object:
        """
        Remove an item from this Container.
        """
        raise NotImplementedError

    def is_empty(self) -> bool:
        """
        Return whether this container is empty or not (whether there's nothing
        left to remove.)
        """
        raise NotImplementedError


class Stack(Container):
    """
    An implementation of Stack.
    """

    def __init__(self) -> None:
        """
        Initialize this Stack.

        >>> s = Stack()
        >>> s.is_empty()
        True
        """
        self._content = []

    def add(self, value: object) -> None:
        """
        Add value this Stack.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        self._content.append(value)

    def remove(self) -> object:
        """
        Remove an item from the top of this Stack.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add("A")
        >>> s.remove()
        'A'
        """
        return self._content.pop()

    def is_empty(self) -> bool:
        """
        Return whether this Stack is empty or not (whether there's nothing
        left to remove.)

        >>> s = Stack()
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        return self._content == []


class Queue(Container):
    """
    An implementation of Stack.
    """

    def __init__(self) -> None:
        """
        Initialize this Stack.

        >>> q = Queue()
        >>> q.is_empty()
        True
        """
        self._content = []

    def add(self, value: object) -> None:
        """
        Add value this Stack.

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        """
        self._content.append(value)

    def remove(self) -> object:
        """
        Remove an item from the top of this Stack.

        >>> q = Queue()
        >>> q.add(5)
        >>> q.add("A")
        >>> q.remove()
        5
        """
        return self._content.pop(0)

    def is_empty(self) -> bool:
        """
        Return whether this Stack is empty or not (whether there's nothing
        left to remove.)

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        """
        return self._content == []