""""This module includes the logic for a merge sort of a given array."""


class Merge:
    """"Class that allows to use functions for merge sorting."""

    @staticmethod
    def sort(array, array_size, reverse=False):
        """"
        It orders an array.
        Complexity: O(n log n)
        :param array: list or tuple for that represents the array.
        :param array_size: Integer value with the number of elements -1.
        :param reverse: Boolean value to decide the sorting direction.

        :return None
        """
        index = 0
        if reverse:
            if array_size > 1:
                # Divide array in 2 parts
                mid = int(array_size / 2)
                left = array[:mid]
                right = array[mid:]

                # Call recursively until get the atomic array
                left = Merge.sort(left, len(left), reverse)
                right = Merge.sort(right, len(right), reverse)

                # Sorting given arrays
                index_l = index_r = index = 0
                left_size, right_size = len(left), len(right)
                while index_l < left_size and index_r < right_size:
                    if left[index_l] > right[index_r]:
                        array[index] = left[index_l]
                        index_l += 1
                    else:
                        array[index] = right[index_r]
                        index_r += 1
                    index += 1

                # There is a chance where only 1 array was read completely,
                # and the other is not yet added. So, here we check for any missing element
                while index_l < left_size:  # Adding the remaining, they are already ordered
                    array[index] = left[index_l]
                    index_l += 1
                    index += 1
                while index_r < right_size:
                    array[index] = right[index_r]
                    index_r += 1
                    index += 1

            return array
        else:
            if array_size > 1:
                # Divide array in 2 parts
                mid = int(array_size / 2)
                left = array[:mid]
                right = array[mid:]

                # Call recursively until get the atomic array
                left = Merge.sort(left, len(left), reverse)
                right = Merge.sort(right, len(right), reverse)

                # Sorting given arrays
                index_l = index_r = index = 0
                left_size, right_size = len(left), len(right)
                while index_l < left_size and index_r < right_size:
                    if left[index_l] < right[index_r]:
                        array[index] = left[index_l]
                        index_l += 1
                    else:
                        array[index] = right[index_r]
                        index_r += 1
                    index += 1

                # There is a chance where only 1 array was read completely,
                # and the other is not yet added. So, here we check for any missing element
                while index_l < left_size:  # Adding the remaining, they are already ordered
                    array[index] = left[index_l]
                    index_l += 1
                    index += 1
                while index_r < right_size:
                    array[index] = right[index_r]
                    index_r += 1
                    index += 1

            return array


if __name__ == "__main__":
    import random
    import time

    test_array = [random.randint(0, 100) for _ in range(0, 100)]
    print("Original array: {}".format(test_array))
    initial_time = time.time()
    Merge.sort(test_array, len(test_array), reverse=False)
    final_time = time.time() - initial_time
    print("Sorted array:   {}".format(test_array))
    print("The sorting took {}s".format(final_time))
