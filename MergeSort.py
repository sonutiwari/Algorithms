import random, time
"""A class to implement Merge sort."""
class MergeSort(object):
    """A class to implement insrtion sort.

    To use:
    >>> is = MergeSort()
    >>> is.Merge_sort_ascending([2, 3, 1, 9, 8, 5, 4, 6, 7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> is.Merge_sort_descending([2, 3, 1, 9, 8, 5, 4, 6, 7])
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    def __init__(self, list_of_nums):
        self.__list__ = list_of_nums

    def sort(self):
        self.__merge_sort_ascending__(0, len(self.__list__) - 1)
        return self.__list__

    def __merge__(self, start, mid, end):
        len_subarray1 = mid - start + 1
        len_subarray2 = end - mid
        left_subarray = []
        right_subarray = []
        for i in range(len_subarray1):
            left_subarray.append(self.__list__[start + i])
        for i in range(len_subarray2):
            right_subarray.append(self.__list__[mid + i + 1])
        i = 0
        j = 0
        for k in range(start, end + 1):
            if i == len_subarray1:
                self.__list__[k] = right_subarray[j]
                j += 1
                continue
            if j == len_subarray2:
                self.__list__[k] = left_subarray[i]
                i += 1
                continue
            if left_subarray[i] <= right_subarray[j] :
                self.__list__[k] = left_subarray[i]
                i += 1
            else:
                self.__list__[k] = right_subarray[j]
                j += 1
        
    def __merge_sort_ascending__(self, start, end) -> list:
        """ The method for Merge sort.
        Args:
            list_of_nums: list of random integers.
            start: lower index of array 
            end: last index of array to be sorted.
        Returns:
            list_of_nums: list of integers in sorted(Ascending) order.
        """
        if end > start:
            mid = (start + end) // 2
            self.__merge_sort_ascending__(start, mid)
            self.__merge_sort_ascending__(mid + 1, end)
            self.__merge__(start, mid, end)

# Testing the code.
mergeSort = MergeSort([2, 3, 1, 9, 8, 5, 4, 6, 7])
print(mergeSort.sort())

# Testing the runtime in realtime.
integers = [0] * 100000 # placeholder for 100K integers.

# Generating 10k integers randomly.
for i in range(100000):
    integers[i] = random.randint(10000, 1000009800) + 1

# Showing runtime of Merge sort for 10k elements.
# ideally it should take around 10 seconds in a normal 
# laptop but it may vary depending on configuration of 
# System used to run the method.
mergeSort = MergeSort(integers)
start_time = time.time()
mergeSort.sort()
print("--- %s seconds ---" % (time.time() - start_time))  