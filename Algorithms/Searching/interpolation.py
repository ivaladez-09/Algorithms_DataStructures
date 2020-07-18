""""This module includes the logic for a interpolation search of a given array."""


class Interpolation:
    """"Class that allows to use functions for interpolation searching.
        It is an improved variant of binary searching."""

    @staticmethod
    def search(value_to_search, array_size, array):
        """"
        It looks for a specific value in an array and returns its index.
        Note: The array shall be in sorted order.
        Complexity: O(log n)
        :param value_to_search: Value of any type to look for.
        :param array_size: Integer value with the number of elements -1.
        :param array: list or tuple for that represents the array.

        :return None for error, Integer that represents the index of the arrays where the
                value_to_search was found.
        """
        low = int(0)
        high = int(array_size) - 1
        mid = -1  # Not valid position
        while value_to_search != mid:
            if low == high:
                break  # Target not found
            mid = int(low +
                      (((high - low) / (array[high] - array[low])) *
                       (value_to_search - array[low]))
                      )  # Get the mid index
            if value_to_search == array[mid]:
                return mid
            elif value_to_search > array[mid]:
                low = mid + 1
            elif value_to_search < array[mid]:
                high = mid - 1
        return None


if __name__ == "__main__":
    import random
    import time

    test_array = [random.randint(0, 10000) for _ in range(0, 1000000)]
    test_array.append(10001)
    value_to_find = 10001  # Look for last item
    sorted(test_array)  # For this technique tha array shall be ordered
    initial_time = time.time()
    test_array_index = Interpolation.search(value_to_find, len(test_array), test_array)
    final_time = time.time() - initial_time
    if test_array_index:
        print("The value {} was found in index {}.".format(value_to_find, test_array_index))
    else:
        print("The value {} was not found.".format(value_to_find))

    print("The searching took {}s".format(final_time))
    # print("The array was: {}".format(test_array))
