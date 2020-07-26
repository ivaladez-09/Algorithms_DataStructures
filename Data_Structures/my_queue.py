"""This module contains a queue structure and its corresponding methods.
    Note: The file can not be called queue.py and the Class neither can be called Queue
          because those names are already used for other built in modules in Python"""


class MyQueue:
    """Class to create the object queue and being able to manipulate as it."""

    def __init__(self, size=10):
        """
        Init the front and rear pointers and the queue using a list of python with a 'fixed' size
        :param size: Integer with the fixed size of the queue
        """
        # [i0, i1, i3, i4]
        self.max_size = size - 1
        self.min_size = 0
        self.front = -1  # index from first enqueue item
        self.rear = -1  # index from last enqueue item
        self.queue = [None for _ in range(0, int(size))]

    def _peek(self):
        """
        Gets the element at the front of the queue without removing it.
        :return The front element from the queue
        """
        return self.queue[self.front]

    def _is_full(self):
        """
        Returns True or False depending if the max capacity of the queue is reached
        :return Boolean that says if the queue is full or not
        """
        return True if self.rear == self.max_size else False

    def _is_empty(self):
        """
        Returns True or False depending if there are no more elements in the queue
        :return Boolean that says if the queue is empty or not
        """
        return True if self.front < self.min_size or self.front > self.rear else False

    def enqueue(self, value):
        """
        Returns True or False depending if there are no more space to add a value in the queue
        :param value: Any type value to be stored in the top of the queue
        :return Boolean that says if the operation o 'push' was possible or not.
        """
        if self._is_full():
            return False
        if self.rear == -1:  # Init front pointer at the first enqueued element
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = value
        return True

    def dequeue(self):
        """
        Returns True or False depending if there are no more elements in the queue
        :return Boolean that says if the operation o 'push' was possible or not.
        """
        if self._is_empty():
            self.front, self.rear = -1, -1  # Re-init pointers for using full queue capacity
            return False
        self.queue[self.front] = None
        self.front += 1
        return True

    def traverse(self):
        """
        Print all the queue elements one by one.
        """
        print("\n")
        index = self.front
        while self.rear >= index != -1:  # If index == -1, means that the queue is empty
            print("Index {} = {}".format(index, self.queue[index]))
            index += 1


if __name__ == "__main__":
    queue = MyQueue(size=10)
    queue.enqueue('H')
    queue.enqueue('e')
    queue.enqueue('l')
    queue.enqueue('l')
    queue.enqueue('o')
    queue.traverse()

    queue.dequeue()
    queue.dequeue()
    queue.traverse()

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.traverse()

    queue.enqueue('B')
    queue.enqueue('y')
    queue.enqueue('e')
    queue.enqueue('!')
    queue.traverse()
