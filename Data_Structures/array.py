"""This module contains an array structure and its corresponding methods."""


class Array:
    """Class to create the object array and being able to manipulate as it."""

    def __init__(self, size=1):
        """
        Implements the array as a list in Python. Initialize the array with zeros.
        :param size: Integer with the fixed size of the array.
        """
        self.array = [None for n in range(0, int(size))]

    def traverse(self):
        """
        Print all the array elements one by one.
        """
        print("\n")
        index = 0
        for element in self.array:
            print("Index {} = {}".format(index, element))
            index += 1

    def insertion(self, index, value):
        """
        Adds an element at the given index.
        :param index: Integer with the array position to insert the value
        :param value: Any type value to be inserted
        """
        if self.array[int(index)] is None:
            self.array[int(index)] = value

    def deletion(self, index):
        """
        Adds an element at the given index.
        :param index: Integer with the array position to delete the value
        """
        if self.array[int(index)]:
            self.array[int(index)] = None

    def search(self, index=None, value=None):
        """
        Adds an element at the given index.
        :param index: Integer with the array position to search
        :param value: Any type value to be searched

        :return Any type value that match the parameters
        """
        if index:
            return self.array[int(index)]
        elif value:
            # return list(filter(lambda x: x == value, self.array))[0]
            searched_value = [n for n in self.array if n == value]
            return searched_value[0] if searched_value else None

    def update(self, index, value):
        """
        Updates an element at the given index.
        :param index: Integer with the array position to update the value
        :param value: Any type value to be updated
        """
        if self.array[int(index)]:
            self.array[int(index)] = value


if __name__ == "__main__":
    arr = Array(8)
    arr.traverse()
    arr.insertion(index=4, value=23)
    arr.insertion(index=1, value=13)
    arr.insertion(index=6, value=2)
    arr.traverse()
    arr.deletion(6)
    arr.traverse()
    print(arr.search(index=4))
    print(arr.search(value=23))
    arr.update(index=4, value=68)
    print(arr.search(index=4))
