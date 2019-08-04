class QuickSort(object):
    """Implement a quicksort.
    """
    def quickSort(self, dataset, first, last) -> list:
        """Recusrsive quick sort algorithm implementation.
        Args:
            dataset: array of integers.
            first: first index.
            last: last index.
        Returns:
            dataset: sorted array of integers.
        """
        if first < last:
            # calculate the split point
            pivotIdx = self.partition(dataset, first, last)

            # now sort the two partitions
            self.quickSort(dataset, first, pivotIdx-1)
            self.quickSort(dataset, pivotIdx+1, last)


    def partition(self, datavalues, first, last) -> int:
        """partition to get our pivot.
        Args:
            datavalues: array of integers where we want to find our pivot.
            first: start index of searching pivot.
            last: last index of searching pivot.
        Returns:
            int
        """
        # choose the first item as the pivot value
        pivotvalue = datavalues[first]
        # establish the upper and lower indexes
        lower = first + 1
        upper = last

        # start searching for the crossing point
        done = False
        while not done:
            # advance the lower index
            while lower <= upper and datavalues[lower] <= pivotvalue:
                lower += 1

            # advance the upper index
            while datavalues[upper] >= pivotvalue and upper >= lower:
                upper -= 1

            # if the two indexes cross, we have found the split point
            if upper < lower:
                done = True
            else:
                # exchange the two values
                datavalues[lower], datavalues[upper] = datavalues[upper], datavalues[lower] 

        # when the split point is found, exchange the pivot value
        datavalues[first], datavalues[upper] = datavalues[upper], datavalues[first]
        
        # return the split point index
        return upper


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]
qs = QuickSort()
# test the merge sort with data
print(items)
qs.quickSort(items, 0, len(items)-1)
print(items)