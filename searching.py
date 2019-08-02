""" All searching algorithms will be implemented here.
"""
class SearchAlgos(object):
    """ Search algorithms implemented.

    To use:
    >>> search = Search()
    >>> search.linear_search(5, [1, 2, 5, 4, 7, 6, 8, 9, 0])
    2
    """
    def __init__(self, array):
        self.__array__ = array
    
    def search(self, element, binary = False):
        if binary:
            return self.binary_search(element, 0, len(self.__array__) - 1)
        else:
            return self.linear_search(element)

    def __linear_search__(self, num) -> int:
        """look for the element sequentially.
            Args:
                num: The number to be searched
                array: The list of integers where we need to search the number. 
            Returns:
                index: The index of element found in the array.
                    if element not found then return -1.   
        """
        for i, element in enumerate(self.__array__):
            if num == element:
                return i
        return -1

    def __binary_search__(self, element, start, end):
        """Binary search implementation.
            Args:
                array: The list of integers where we need to search the number. 
                element: The element to be searched.
                start: start index of search array
                end: end index of search array.
            Returns:
                index: The index of element found in the array.
                    if element not found then return -1.   
        """
        if start <= end:
            mid = (start + end) // 2
            if self.__array__[mid] == element:
                return mid
            elif self.__array__[mid] > element:
                return self.binary_search(element, 0, mid - 1)
            else:
                return self.binary_search(element, mid+1, end)
        else:
            return -1
sa = SearchAlgos([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sa.search(1, True))
print(sa.search(10))