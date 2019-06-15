"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
import math


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        # should use insert before on the head node
        new_head = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_head
            self.tail = self.head
        else:
            new_head.next = self.head

            self.head.prev = new_head

            self.head = new_head

    def remove_from_head(self):
        if not self.head:
            return None

        value = self.head.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1

        return value

    def add_to_tail(self, value):
        # should calll insert after on the tail node
        self.length += 1
        new_tail = ListNode(value)
        # initiates the list if it is empty
        if not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail

    def remove_from_tail(self):
        if not self.tail:
            return None

        val = self.tail.value

        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev

        self.length -= 1

        return val

    def move_to_front(self, node):
      # checking to see if the list is empty or we are trying to move to the front the head
        if self.length < 2 or node is self.head:
            return
        # checks if it is the tail
        if node is self.tail:
            self.remove_from_tail()
            self.add_to_head(node.value)
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            self.add_to_head(node.value)
            self.length -= 1

    def move_to_end(self, node):
        if self.length < 2 or node is self.tail:
            return

        # checks to see if this is the head
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            self.add_to_tail(node.value)
            self.length -= 1

    def delete(self, node):
        # checks for length of 0 and resets the list
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0

        # checks if the node is the head
        elif node is self.head:
            self.remove_from_head()
        # or the tail
        elif node is self.tail:
            self.remove_from_tail()

        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            self.length -= 1

    def get_max(self):
        # you can optimize it by looping at the same time from the end of the linked list and have a condition like while start is not end do that and every iteration change the start to be start.next and end to be end.prev
        current = self.head
        maxVal = -math.inf

        while current:
            if current.value > maxVal:
                maxVal = current.value

            current = current.next

        return maxVal


myList = DoublyLinkedList()


myList.add_to_head(1)
myList.add_to_tail(2)
myList.add_to_tail(3)
myList.add_to_tail(4)

myList.move_to_front(myList.head.next.next)

print(myList.head.next.next.value)
