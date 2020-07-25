"""This module contains a stack structure and its corresponding methods."""

class Stack:
    """Class to create the object stack and being able to manipulate as it."""

    def __init__(self, size=10):
        """
        Init the top pointer and the stack using a list of python with a 'fixed' size
        :param size: Integer with the fixed size of the stack
        """
        self.max_size = size - 1
        self.top = -1  # index from Last pushed item
        self.stack = [None for _ in range(0, int(size))]

    def _peek(self):
        """
        Returns the top element from the stack
        :return The last(top) element from the stack
        """
        return self.stack[self.top]

    def _is_full(self):
        """
        Returns True or False depending if the max capacity of the stack is reached
        :return Boolean that says if the stack is full or not
        """
        return True if self.top == self.max_size else False

    def _is_empty(self):
        """
        Returns True or False depending if there are no more elements in the stack
        :return Boolean that says if the stack is empty or not
        """
        return True if self.top < 0 else False

    def push(self, value):
        """
        Returns True or False depending if there are no more space to add a value in the stack
        :param value: Any type value to be stored in the top of the stack
        :return Boolean that says if the operation o 'push' was possible or not.
        """
        if self._is_full():
            return False
        self.top += 1
        self.stack[self.top] = value
        return True

    def pop(self):
        """
        Returns True or False depending if there are no more elements in the stack
        :return Boolean that says if the operation o 'push' was possible or not.
        """
        if self._is_empty():
            return False
        self.stack[self.top] = None
        self.top -= 1
        return True

    def traverse(self):
        """
        Print all the stack elements one by one.
        """
        print("\n")
        index = 0
        while index <= self.top:
            print("Index {} = {}".format(index, self.stack[index]))
            index += 1


if __name__ == "__main__":
    stack = Stack(size=10)
    stack.push('H')
    stack.push('e')
    stack.push('l')
    stack.push('l')
    stack.push('o')
    stack.traverse()

    stack.pop()
    stack.pop()
    stack.traverse()
