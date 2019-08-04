import random, time
"""A class to implement insertion sort."""
class InsertionSort(object):
    """A class to implement insrtion sort.

    To use:
    >>> is = InsertionSort()
    >>> is.insertion_sort_ascending([2, 3, 1, 9, 8, 5, 4, 6, 7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> is.insertion_sort_descending([2, 3, 1, 9, 8, 5, 4, 6, 7])
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    def insertion_sort_ascending(self, list_of_nums) -> list:
        """ The method for insertion sort.
        Args:
            list_of_nums: list of random integers.
        Returns:
            list_of_nums: list of integers in sorted(Ascending) order.
        """
        for j in range(1, len(list_of_nums)):
            key = list_of_nums[j] #pivot
            i = j - 1 #Start scanning already sorted list from Right.
            while i >= 0 and list_of_nums[i] > key:
                list_of_nums[i + 1] = list_of_nums[i] #Keep shifting each element to the right 
                #by 1 place until right place is found for insertion.
                i -= 1
            list_of_nums[i + 1] = key #insert element.
        return list_of_nums

    def insertion_sort_descending(self, list_of_nums) -> list:
        """ The method for normal insertion sort.
        Args:
            list_of_nums: list of random integers.
        Returns:
            list_of_nums: list of integers in sorted(Descending) order.
        """
        for j in range(1, len(list_of_nums)):
            key = list_of_nums[j]
            i = j - 1
            while i >= 0 and list_of_nums[i] < key:
                list_of_nums[i + 1] = list_of_nums[i]
                i -= 1
            list_of_nums[i + 1] = key
        return list_of_nums

# Testing the code.
insSort = InsertionSort()
print(insSort.insertion_sort_descending([2, 3, 1, 9, 8, 5, 4, 6, 7]))

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
insSort.insertion_sort_ascending(integers)
print("--- %s seconds ---" % (time.time() - start_time))  