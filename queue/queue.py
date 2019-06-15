class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        # actually if we want constant time for both operations we might need a doubly linked list
        self.storage = {}
        self.head = None
        self.tail = None

    def enqueue(self, item):
        # if the queue has nothing in it, initiate both head and tail to be at position 0 and store the item in the dictionary under that key, increment the storage
        if self.size == 0:

            self.head = 0
            self.tail = 0
            self.storage[self.tail] = item
        else:
            # else put the item at the position of the tail + 1 and increment it as well
            self.tail += 1
            self.storage[self.tail] = item

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            # check if the size is 1, then return the element and put tail and head to be none again
            item = self.storage[self.tail]
            self.tail = None
            self.head = None

            self.size = 0

            return item
        else:
            # else get the item at the position of the head and return it, but increment the head by one
            item = self.storage[self.head]
            self.head += 1

            self.size -= 1

            return item

    def len(self):
        return self.size
