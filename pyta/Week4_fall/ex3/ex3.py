"""CSC148 Exercise 3: Stacks and a Chain of People

=== CSC148 Fall 2017 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 3.
It is divided into two parts:
- Task 1, which contains two functions you should implement using only
  the public interface of Stacks (initializer, is_empty, push, pop)
- Task 2, which contains the definition of two new classes, Person and
  PeopleChain. You'll have to read their documentation carefully to understand
  how to use them.
"""
from typing import List, Optional
from stack import Stack


##############################################################################
# Task 1: More Stack Exercises
##############################################################################
def reverse(stack: Stack) -> None:
    """Reverse all the elements of <stack>.

    Do nothing if the stack is empty.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    # TODO: implement this function.
    if stack.is_empty(): return
    temp = []
    while not stack.is_empty():
        temp.append(stack.pop())
    temp = temp[::-1]
    while len(temp) != 0:
        stack.push(temp.pop())



def merge_alternating(stack1: Stack, stack2: Stack) -> Stack:
    """Return a stack by merging two stacks in alternating order.

    Precondition: <stack1> and <stack2> have the same size.

    The new stack's top element is the top element of <stack1>,
    followed by the top element of <stack2>, followed by the next element
    of <stack1>, then <stack2>, etc.

    If <stack1> and <stack2> are both empty, the new stack should also be empty.

    <stack1> and <stack2> should be unchanged when the function ends.

    >>> s1 = Stack()
    >>> s2 = Stack()
    >>> s1.push('a')
    >>> s1.push('b')
    >>> s1.push('c')
    >>> s2.push(1)
    >>> s2.push(2)
    >>> s2.push(3)
    >>> merged = merge_alternating(s1, s2)
    >>> merged.pop()
    'c'
    >>> merged.pop()
    3
    >>> merged.pop()
    'b'
    >>> merged.pop()
    2
    >>> merged.pop()
    'a'
    >>> merged.pop()
    1
    >>> merged.is_empty()
    True
    >>> s1.is_empty()
    False
    >>> s2.is_empty()
    False
    """
    # TODO: implement this function.

    def copy_and_reverse_stack(stack):
        """
        copy a stack
        """
        if stack is None: return None
        copy1 = Stack()
        copy2 = Stack()
        while not stack.is_empty():
            value = stack.pop()
            copy1.push(value)
            copy2.push(value)
        while not copy2.is_empty():
            stack.push(copy2.pop())
        return copy1

    result = Stack()
    if stack1.is_empty() and stack2.is_empty():
        return result
    temp1 = copy_and_reverse_stack(stack1)
    temp2 = copy_and_reverse_stack(stack2)
    while not temp2.is_empty():
        result.push(temp2.pop())
        result.push(temp1.pop())
    return result



##############################################################################
# Task 2: A Chain of People
##############################################################################
class ShortChainError(Exception):
    pass


class Person:
    """A person in a chain of people.

    === Attributes ===
    name: The name of this person.
    next: The next person in the chain, or None if this person is not holding
        onto anyone.
    """
    name: str
    next: Optional['Person']

    def __init__(self, name: str) -> None:
        """Initialize a person with the given name.

        The new person initially is not holding onto anyone.
        """
        self.name = name
        self.next = None  # Initially holding onto no one


class PeopleChain:
    """A chain of people.

    === Attributes ===
    leader: the first person in the chain, or None if the chain is empty.
    """
    leader: Optional['Person']

    def __init__(self, names: List[str]) -> None:
        """Initialize people linked together in the order provided in <names>.

        The leader of the chain is the first person in <names>.
        """
        if names == []:
            # No leader, representing an empty chain!
            self.leader = None
        else:
            # Initialize leader
            self.leader = Person(names[0])
            current_person = self.leader
            for name in names[1:]:
                # Set the link for the current person
                current_person.next = Person(name)
                # Update the current person
                # Note that current_person always refers to
                # the LAST person in the chain
                current_person = current_person.next

    # TODO: Implement this method!
    def get_leader(self) -> str:
        """Return the name of the leader of the chain.

        Raise ShortChainError if chain has no leader.

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_leader()
        'Iron Man'
        """
        if self.leader is None:
            raise ShortChainError
        return self.leader.name

    # TODO: Implement this method!
    def get_second(self) -> str:
        """Return the name of the second person in the chain.

        That is, return the name of the person the leader is holding onto.
        Raise ShortChainError if chain has no second person.

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_second()
        'Janna'
        """
        if not self.leader.next:
            raise ShortChainError
        return self.leader.next.name

    # TODO: Implement this method!
    def get_third(self) -> str:
        """Return the name of the third person in the chain.

        Raise ShortChainError if chain has no third person.

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_third()
        'Kevan'
        """
        if not self.leader.next.next:
            raise ShortChainError
        return self.leader.next.next.name


    # TODO: Implement this method!
    def get_nth(self, n: int) -> str:
        """Return the name of the n-th person in the chain.

        Precondition: n >= 1
        Raise ShortChainError if chain doesn't have n people.
        Indexing here starts at 1 (see doctest for an example).

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_nth(1)
        'Iron Man'
        """
        # Remember: you must use a for or while loop in this function body!
        # If you use a for loop but don't need to use the loop variable,
        # use an underscore for the variable name:
        #
        # for _ in range(10):
        #     <code that doesn't use the index>
        if self.leader == None:
            raise ShortChainError
        cur = self.leader
        for _ in range(n-1):
            cur = cur.next
            if cur is None:
                raise ShortChainError
        return cur.name




if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': [
            'typing', 'doctest', 'python_ta', 'stack'
        ]
    })