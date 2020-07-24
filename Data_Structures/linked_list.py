"""This module contains a linked list structure and its corresponding methods."""


class Node:
    """Basic structure"""

    def __init__(self, val):
        """"""
        self.data = val
        self.next = None

    def get_data(self):
        """"""
        return self.data

    def get_next(self):
        """"""
        return self.next

    def set_data(self, val):
        """"""
        self.data = val

    def set_next(self, val):
        """"""
        self.next = val


class LinkedList:
    """Class to create the object linked list and being able to manipulate as it."""

    def __init__(self):
        """
        Init the head pointer to None
        """
        self.head = None

    def traverse(self):
        """
        Print all the linked list elements one by one.
        """
        print("\n\t=== Traverse ===")
        current = self.head
        index = 0
        while current:
            print("\tIndex {} = {}".format(index, current.get_data()))
            index += 1
            current = current.get_next()

    def insertion(self, index, value):
        """
        Adds an element at the given index.
        :param index: Integer with the array position to insert the value
        :param value: Any type value to be inserted
        """
        current = self.head
        previous = None
        pos = 0
        new_node = Node(value)
        if index == 0:
            self.head = new_node
            new_node.set_next(None)
        else:
            while current and pos < index:
                previous = current
                current = current.get_next()
                pos += 1
            previous.set_next(new_node)
            new_node.set_next(current)

    def deletion(self, index):
        """
        Adds an element at the given index.
        :param index: Integer with the array position to delete the value
        """
        current = self.head
        previous = None
        count = 0
        while current:
            if count == index and previous:
                previous.set_next(current.get_next())
                del current
                break
            previous = current
            current = current.get_next()
            count += 1

    def search(self, index=None, value=None):
        """
        Search of an element at the given index or value.
        :param index: Integer with the array position to search
        :param value: Any type value to be searched

        :return If parameter selected is index, return the value
                If parameter selected is value, return the index
        """
        if index:
            count = 0
            current = self.head
            while current and count < index:
                count += 1
                current = current.get_next()
            if count > 0:
                return current.get_data()
        elif value:
            count = 0
            current = self.head
            while current:
                if current.get_data() == value:
                    return count
                count += 1
                current = current.get_next()


if __name__ == "__main__":
    LL = LinkedList()
    LL.insertion(0, 'H')
    LL.insertion(1, 'e')
    LL.insertion(2, 'l')
    LL.insertion(3, 'l')
    LL.insertion(4, 'o')
    LL.traverse()
    LL.deletion(1)
    LL.deletion(3)
    LL.traverse()
    LL.insertion(1, 'e')
    LL.insertion(4, 'o')
    LL.traverse()
    print("\n\tIndex 4 value: {}".format(LL.search(index=4)))
    print("\tValue 'o' in index: {}".format(LL.search(value='o')))
