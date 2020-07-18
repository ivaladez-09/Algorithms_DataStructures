""""This module includes the logic for a bubble sort of a given array."""


class Bubble:
    """"Class that allows to use functions for bubble sorting."""

    @staticmethod
    def sort(array, array_size, reverse=False):
        """"
        It orders an array.
        Complexity: O(n²)
        :param array: list or tuple for that represents the array.
        :param array_size: Integer value with the number of elements -1.
        :param reverse: Boolean value to decide the sorting direction.

        :return None
        """
        swap_count = -1
        if reverse:
            while swap_count != 0:
                swap_count = 0
                index = 0
                while (index + 1) < array_size:
                    if array[index] < array[index + 1]:
                        array[index], array[index + 1] = array[index + 1], array[index]
                        swap_count += 1
                    index += 1
        else:
            while swap_count != 0:
                swap_count = 0
                index = 0
                while (index + 1) < array_size:
                    if array[index] > array[index + 1]:
                        array[index], array[index + 1] = array[index + 1], array[index]
                        swap_count += 1
                    index += 1


if __name__ == "__main__":
    import random
    import time

    test_array = [random.randint(0, 100) for _ in range(0, 100)]
    print("Original array: {}".format(test_array))
    initial_time = time.time()
    Bubble.sort(test_array, len(test_array), reverse=False)
    final_time = time.time() - initial_time
    print("Sorted array:   {}".format(test_array))
    print("The sorting took {}s".format(final_time))
