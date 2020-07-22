""""This module includes the logic for a quick sort of a given array."""


class Quick:
    """"Class that allows to use functions for quick sorting."""

    @staticmethod
    def _partition(arr, low, high, reverse=False):
        """"
        It orders an array.
        :param arr: list or tuple for that represents the array.
        :param low: Index of the low part of the array.
        :param high: Index of the high part of the array.
        :param reverse: Boolean value to decide the sorting direction.

        :return Integer with the partition index
        """
        if reverse:
            i = low - 1  # End of array + 1
            pivot = arr[high]

            # Always knowing where is the last value that was smaller than the pivot, so,
            # we can in a later iteration swap that value with a bigger than the pivot.
            for j in range(low, high):
                if arr[j] > pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            # Swap to the corresponding position for the pivot
            partition_index = i + 1
            arr[partition_index], arr[high] = arr[high], arr[partition_index]

            return partition_index
        else:
            i = low - 1  # Beginning of array - 1
            pivot = arr[high]

            # Always knowing where is the last value that was smaller than the pivot, so,
            # we can in a later iteration swap that value with a bigger than the pivot.
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            # Swap to the corresponding position for the pivot
            partition_index = i + 1
            arr[partition_index], arr[high] = arr[high], arr[partition_index]

            return partition_index

    @staticmethod
    def _sorting(arr, low, high, reverse=False):
        """"
        It orders an array.
        Complexity: O(n²)
        :param arr: list or tuple for that represents the array.
        :param low: Index of the low part of the array.
        :param high: Index of the high part of the array.
        :param reverse: Boolean value to decide the sorting direction.

        :return None
        """
        if low < high:
            # Order the array in left (smaller than pivot) and right (bigger than pivot)
            pi = Quick._partition(arr, low, high, reverse)

            # Split the array in two
            Quick._sorting(arr, low, pi - 1, reverse)
            Quick._sorting(arr, pi + 1, high, reverse)

    @staticmethod
    def sort(array, array_size, reverse=False):
        """"
        Interface for Quick Sort. It orders an array.
        Complexity: O(n²)
        :param array: list or tuple for that represents the array.
        :param array_size: Integer value with the number of elements -1.
        :param reverse: Boolean value to decide the sorting direction.

        :return None
        """
        Quick._sorting(arr=array, low=0, high=array_size - 1, reverse=reverse)


if __name__ == "__main__":
    import random
    import time

    test_array = [random.randint(0, 100) for _ in range(0, 100)]
    print("Original array: {}".format(test_array))
    initial_time = time.time()
    Quick.sort(test_array, len(test_array), reverse=True)
    final_time = time.time() - initial_time
    print("Sorted array:   {}".format(test_array))
    print("The sorting took {}s".format(final_time))
