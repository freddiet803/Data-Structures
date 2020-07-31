"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value <= self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            # do this
            if self.left is not None:
                contained = self.left.contains(target)
                if contained:
                    return True
                else:
                    return False
        elif target > self.value:  # what we do because target is greater than self.value
            if self.right is not None:
                contained = self.right.contains(target)
                if contained:
                    return True
                else:
                    return False
        else:
            return False
    # Return the maximum value found in the tree

    def get_max(self):
        current_max = self.value
        if self.right is not None:
            return self.right.get_max()
        else:
            return current_max

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)

        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        from collections import deque
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()  # following FIFO remove the first node in queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        stack = []
        stack.append(self)

        while len(stack) > 0:  # stacks are LIFO and grabbing right first should give dpth first traversal
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
print(bst.right.left.value)
print(bst.contains(77))
print(bst.get_max())

bst.bft_print()
bst.dft_print()
print('####################################################################################')
bst.in_order_print()
#print("elegant methods")
#print("pre order")
# bst.pre_order_dft()
#print("in order")
# bst.in_order_dft()
#print("post order")
# bst.post_order_dft()
