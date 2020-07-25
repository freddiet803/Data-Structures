"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    def delete_node(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:  # our list is empty
            self.head = new_node
            self.tail = new_node
        else:
            # take current head and set its prev to the new node
            self.head.set_prev(new_node)
            # set the new nodes next to the current head
            new_node.set_next(self.head)
            self.head = new_node    # set the head to the new node

        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        elif self.head == self.tail:
            value_removed = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value_removed
        else:
            value_removed = self.head.get_value()
            self.head = self.head.get_next()
            self.head.prev = None
            self.length -= 1
            return value_removed

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.tail and not self.head:
            return None
        elif self.head == self.tail:
            value_removed = self.tail.get_value()
            self.tail = None
            self.head = None
            self.length -= 1
            return value_removed
        else:
            value_removed = self.tail.get_value()
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
            self.length -= 1
            return value_removed

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        if not self.tail and not self.head:
            return None
        elif self.tail == self.head:
            self.tail = None
            self.head = None

        elif node.prev == None:  # if the node is the head so i could say if node is self.head
            node.next.prev = None
            self.head = node.next
            # node.delete_node()

        elif node.next == None:  # if node is the tail or 'if node is self.tail' which would have a next of none
            node.prev.next = None
            self.tail = node.prev
            # node.delete_node()

        else:   # node in middle
            node.prev.next = node.next
            node.next.prev = node.prev
            # node.delete_node()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        if not self.head and not self.tail:
            return None
        elif self.tail == self.head:
            return self.head.get_value()
        else:
            currentMax = self.head.get_value()
            theHead = self.head

            while theHead.get_next() is not None:
                neighborNode = theHead.get_next()
                if neighborNode.get_value() > currentMax:
                    currentMax = neighborNode.get_value()
                theHead = theHead.get_next()
            return currentMax


p = DoublyLinkedList()

print(p.length)
p.add_to_tail(10)
print(p.length)
print(p.head.get_value())
print(p.tail.get_value())
#print(p.remove_from_tail(), 'the return')

print(p.length)

p.add_to_tail(15)
print(p.length)
print(p.head.get_value())
print(p.tail.get_value())
print(p.get_max())
'''p.delete(p.head)
print(p.length)
print(p.head.get_value())'''

# p.remove_from_tail()
'''print(p.length)
print(p.head.get_value())
print(p.tail.get_value())'''
