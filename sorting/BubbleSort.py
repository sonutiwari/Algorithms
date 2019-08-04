class BubbleSort(object):
    """Implementation of bubble sort algorithm.
    """
    def bubble_sort_ascending(self, array):
        """Bubble sort algorithm in ascending order.
        Args:
            array: array of integers.
        Returns:
            array: array of integers in sorted order(ascending)
        """
        N = len(array)
        for i in range(N - 1):
            for j in range(N - 1, i, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
        return array
bs = BubbleSort()
print(bs.bubble_sort_ascending([9, 6, 7, 8, 5, 3, 4, 1, 2]))