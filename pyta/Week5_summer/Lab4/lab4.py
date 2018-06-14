from typing import Union, Any
class LinkedListNode:
    """
    A Node to be used in a LinkedList.

    next_ - The successor to this LinkedListNode
    value - The data represented by this LinkedListNode.
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next: Union["LinkedListNode", None] = None) -> None:
        """
        Initialize this LinkedListNode with the value value and successor next.

        >>> LinkedListNode(3).value
        3
        >>> LinkedListNode(3).next_ == None
        True
        """
        self.value = value
        self.next_ = next

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedListNode.

        >>> print(LinkedListNode(3))
        3 ->
        """
        return "{} -> ".format(self.value)

class LinkedList:
    """
    Collection of LinkedListNodes.

    front - first node of this LinkedList
    back - last node of this LinkedList
    size - the number of nodes in this LinkedList (>= 0)
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Initialize an empty LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.size
        0
        """
        self.front = None
        self.back = None
        self.size = 0

    def prepend(self, value: Any) -> None:
        """
        Insert value to the start of this LinkedList (before self.front).

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        self.front = LinkedListNode(value, self.front)
        if self.back is None:
            self.back = self.front
        self.size += 1

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        cur_node = self.front
        result = ''
        while cur_node is not None:
            result += str(cur_node)
            cur_node = cur_node.next_
        return result + '|'

    def find_second_last(self):
        """
        return the second last node
        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(3)
        >>> print(lnk)
        3 -> 2 -> 1 -> 0 -> |
        """
        # >>> print(lnk.find_second_last())
        # 1 ->
        if self.size < 2:
            return None
        current = self.front
        while current.next_.next_ is not None:
            current = current.next_
        return current

    def get_value(self):
        """
        return a list contains all the value of the linked list
        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(3)
        >>> print(lnk.get_value())
        [3, 2, 1, 0]
        """
        result = []
        current = self.front
        while current is not None:
            result.append(current.value)
            current = current.next_
        return result

    def __eq__(self, other):
        """
        return True if and only if
        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(3)
        >>> other = LinkedList()
        >>> other.prepend(0)
        >>> other.prepend(1)
        >>> other.prepend(2)
        >>> other.prepend(3)
        >>> print(lnk == other)
        True
        """
        # Approach one
        return self.size == other.size and self.get_value() == other.get_value()
        # cur_self = self.front
        # cur_other = other.front
        # while cur_self is not None:
        #     if cur_other.value != cur_self.value:
        #         return False
        #     cur_self = cur_self.next_
        #     cur_other = cur_other.next_
        # return self.size == other.size

    def find_value(self, value):
        """
        find a given value
        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(3)
        >>> print(lnk.find_value(44))
        None
        >>> print(lnk.find_value(2))
        2 ->
        """
        current = self.front
        while current is not None:
            if current.value == value:
                return current
            current = current.next_
        return None

    def add_after(self, value, position_value):
        """
        add the value after the position
        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(3)
        >>> lnk.add_after(4, 3)
        >>> print(lnk)
        3 -> 4 -> 2 -> 1 -> 0 -> |
        """
        current = self.find_value(position_value)
        temp = current.next_
        current.next_ = LinkedListNode(value, temp)

    def add_after_every(self, value, position_value):
        """
        add a  value in every position value
        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(3)
        >>> print(lnk)
        3 -> 2 -> 1 -> 2 -> 0 -> |
        >>> lnk.add_after_every(4, 2)
        >>> print(lnk)
        3 -> 2 -> 4 -> 1 -> 2 -> 4 -> 0 -> |
        """
        current = self.front
        while current is not None:
            if current.value == position_value:
                temp = current.next_
                current.next_ = LinkedListNode(value, temp)
            current = current.next_









