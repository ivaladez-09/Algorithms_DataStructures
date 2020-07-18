""""This module includes the logic for a linear search of a given array."""


class Linear:
    """"Class that allows to use functions for linear searching."""

    @staticmethod
    def search(value_to_search, array_size, array):
        """"
        It looks for a specific value in an array and returns its index.
        Complexity: O(n)
        :param value_to_search: Value of any type to look for.
        :param array_size: Integer value with the number of elements -1.
        :param array: list or tuple for that represents the array.

        :return None for error, Integer that represents the index of the arrays where the
                value_to_search was found.
        """
        index = int(0)
        size = int(array_size)
        while index < size:
            if array[index] == value_to_search:
                return index
            index += 1
        return None


if __name__ == "__main__":
    import random
    import time

    test_array = [random.randint(0, 10000) for _ in range(0, 1000000)]
    test_array.append(10001)
    value_to_find = 10001  # Look for last item
    initial_time = time.time()
    test_array_index = Linear.search(value_to_find, len(test_array), test_array)
    final_time = time.time() - initial_time
    if test_array_index:
        print("The value {} was found in index {}.".format(value_to_find, test_array_index))
    else:
        print("The value {} was not found.".format(value_to_find))

    print("The searching took {}s".format(final_time))
    # print("The array was: {}".format(test_array))
