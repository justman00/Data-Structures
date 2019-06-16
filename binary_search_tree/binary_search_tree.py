import math


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # store the comparator in a placeholder

        # start a while loop on the condition of while we can actually place the given value inside the tree

        # compare our value with the comparator and move in the needed direction

        # if we find that is is bigger or smaller and left or right are None put it there

        comparator = self
        new_tree = BinarySearchTree(value)

        while comparator:
            if comparator.value > value:
                if not comparator.left:
                    comparator.left = new_tree
                    break
                else:
                    comparator = comparator.left
            elif comparator.value < value:
                if not comparator.right:
                    comparator.right = new_tree
                    break
                else:
                    comparator = comparator.right

    def contains(self, target):
        # loop over every single node in the tree and compare that value with the one we have, if it is equal return true, if it is bigger or smaller move in that direction
        current = self
        while current:
            if current.value == target:
                return True
            elif current.value > target:
                current = current.left
            else:
                current = current.right

        return False

    def get_max(self):
        # we have to loop over every single value in our tree and add it up to our placeholder data
        # to find the max we would need to go only to the right

        max_value = -math.inf

        current = self

        while current:
            if current.value > max_value:
                max_value = current.value

            current = current.right

        return max_value

    def for_each(self, cb):
        # loop over every value and call the cb
        # do this thing for every single node and its left and right if applicable, then move down the tree
        # create another function that would call the cb recursively for every of the left and right except itself
        cb(self.value)

        def helper(node):
            if node.right:
                cb(node.right.value)
                helper(node.right)

            if node.left:
                cb(node.left.value)
                helper(node.left)

        helper(self)


tree = BinarySearchTree(5)

tree.insert(3)
tree.insert(2)

tree.insert(7)
tree.insert(9)
tree.insert(6)
print(tree.get_max())
# print(tree.left.left.value)
# print(tree.right.left.value)
