""" All searching algorithms will be implemented here.
"""
class SearchAlgos(object):
    """ Search algorithms implemented.

    To use:
    >>> search = Search()
    >>> search.linear_search(5, [1, 2, 5, 4, 7, 6, 8, 9, 0])
    2
    """
    def linear_search(self, num, array) -> int:
        """look for the element sequentially.
            Args:
                num: The number to be searched
                array: The list of integers where we need to search the number. 
            Returns:
                index: The index of element found in the array.
                    if element not found then return -1.   
        """
        for i, element in enumerate(array):
            if num == element:
                return i
        return -1