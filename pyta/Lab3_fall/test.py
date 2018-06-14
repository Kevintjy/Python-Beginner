list = []
dict = set()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, node):
        if not self.head:
            self.head = node
        else:
            lastNode = self.head
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = node
        self.size += 1


def delete(linkedlist, value, position):
    lastnode = linkedlist.head
    for i in range(position):
        while lastnode.next.value != value:
            lastnode = lastnode.next
    lastnode.next = lastnode.next.next



a = LinkedList()
a.append(Node(1))
a.append(Node(3))
a.append(Node(4))
a.append(Node(3))
a.append(Node(0))
delete(a, 3, 2)
current = a.head

while current:
    print(current.value, " ")
    current = current.next
