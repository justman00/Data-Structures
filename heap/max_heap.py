import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        size = self.get_size()
        self.storage.append(value)
        if size == 0:
            return
        else:
            self._bubble_up(size)

    def delete(self):
        if self.get_size() == 1:
            value = self.storage[0]
            self.storage = []
            return value
        elif self.get_size() == 0:
            return
        # replace the first item of the array with the last one
        value = self.storage[0]
        last_item = self.storage[-1]
        del self.storage[-1]
        self.storage[0] = last_item
        # once we have a new root, compare it to its children and move into that direction by doing it recursively
        self._shift_down(0)

        return value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # check if index is 0 and break
        if index <= 0:
            return
        # takes the index of an item in the array
        child = self.storage[index]
        # gets its parent and compares with it
        parent_index = math.ceil((index - 2) / 2)
        parent = self.storage[parent_index]
        # if it is bigger swap them and call the function again
        if child > parent:
            self.storage[parent_index] = child
            self.storage[index] = parent
            self._bubble_up(parent_index)
        # if not just break out of the recursive loop
        else:
            return

        pass

    def _shift_down(self, index):
        # get the element
        parent = self.storage[index]
        # get the children as per ecuation
        index_one = (index * 2) + 1
        index_two = (index * 2) + 2

        size = self.get_size() - 1

        # think how to handle it being out of the range
        if index_one > size or index_two > size:
            return

        child_one = self.storage[index_one]
        child_two = self.storage[index_two]
        # check if it is bigger than the children and return out of the recursive loop
        if parent >= child_one and parent >= child_two:
            return
        # else pick the biggest children and move into that direction
        else:
            if child_one >= child_two:
                self.storage[index] = child_one
                self.storage[index_one] = parent
                return self._shift_down(index_one)
            else:
                self.storage[index] = child_two
                self.storage[index_two] = parent
                return self._shift_down(index_two)


myHeap = Heap()

myHeap.insert(6)
myHeap.insert(7)
myHeap.insert(5)
myHeap.insert(8)
myHeap.insert(10)
myHeap.insert(1)
myHeap.insert(2)
myHeap.insert(5)

descending_order = []

while myHeap.get_size() > 0:
    descending_order.append(myHeap.delete())

print(descending_order)
