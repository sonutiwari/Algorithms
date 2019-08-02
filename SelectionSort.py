import random, time
"""A class to implement insertion sort."""
class SelectionSort(object):
    """A class to implement insrtion sort.

    To use:
    >>> is = SelectionSort()
    >>> is.selection_sort([2, 3, 1, 9, 8, 5, 4, 6, 7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> is.insertion_sort_descending([2, 3, 1, 9, 8, 5, 4, 6, 7])
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    def selection_sort(self, list_of_nums) -> list:
        """ The method for selection sort.
        Args:
            list_of_nums: list of random integers.
        Returns:
            list_of_nums: list of integers in sorted(Ascending) order.
        """
        n = len(list_of_nums)
        for j in range(0, n - 1):
            smallest = j
            i = j + 1
            while i < n:
                if list_of_nums[i] < list_of_nums[smallest]:
                    smallest = i
                i += 1
            list_of_nums[smallest], list_of_nums[j] = list_of_nums[j], list_of_nums[smallest]
        return list_of_nums

    def selection_sort_descending(self, list_of_nums) -> list:
        """ The method for normal insertion sort.
        Args:
            list_of_nums: list of random integers.
        Returns:
            list_of_nums: list of integers in sorted(Descending) order.
        """
        n = len(list_of_nums)
        for j in range(0, n - 1):
            largest = j
            i = j + 1
            while i < n:
                if list_of_nums[i] > list_of_nums[largest]:
                    largest = i
                i += 1
            list_of_nums[j], list_of_nums[largest] = list_of_nums[largest], list_of_nums[j]
        return list_of_nums

# Testing the code.
insSort = SelectionSort()
print(insSort.selection_sort([2, 3, 1, 9, 8, 5, 4, 6, 7]))
print(insSort.selection_sort_descending([2, 3, 1, 9, 8, 5, 4, 6, 7]))

# Testing the runtime in realtime.
integers = [0] * 10000 # placeholder for 10k integers.

# Generating 10k integers randomly.
for i in range(10000):
    integers[i] = random.randint(100, 10000000) + 1

# Showing runtime of insertion sort for 10k elements.
# ideally it should take around 10 seconds in a normal 
# laptop but it may vary depending on configuration of 
# System used to run the method.
start_time = time.time()
insSort.selection_sort(integers)
print("--- %s seconds ---" % (time.time() - start_time))  