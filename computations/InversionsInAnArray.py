class InversionInAnArray(object):
    """An inversion is a condition in an array
    Such that for any i<n-1 and j<n we have
    array[i] > array[j] where n is length of
    array. for sorted array no of inversions 
    will be 0.
    """
    def num_of_inversions_naive(self, array) -> int:
        """This algorithm will use exhaustive search to 
        find all the inversions. runtime O(n^2).
        Args:
            array: array of integers.
        Returns:
            int.
        """
        N = len(array)
        count = 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                if array[i] > array[j]:
                    count += 1
        return count

    def modified_merge(self, A, start, mid, end) -> int:
        """Merging two subarrays in one sorted array.
        Args:
            A: array of integers.
            start: start index.
            mid: middle index.
            end: last index.
        Returns:
            int
        """
        num_of_inv = 0
        len_subarray1 = mid - start + 1
        len_subarray2 = end - mid
        left_subarray = [] # left sorted array.
        right_subarray = [] # right sorted array.
        for i in range(len_subarray1):
            left_subarray.append(A[start + i])
        for i in range(len_subarray2):
            right_subarray.append(A[mid + i + 1])
        i = 0
        j = 0
        k = start
        while ((i != len_subarray1) and (j != len_subarray2)):
            if left_subarray[i] <= right_subarray[j]:
                A[k] = left_subarray[i]
                i += 1
            else:
                A[k] = right_subarray[j]
                j += 1
                num_of_inv += j #inversion will occur
            k += 1
        if i == len_subarray1:
            for m in range(j, len_subarray2):
                A[k] = right_subarray[m]
                k += 1
        if j == len_subarray2:
            num_of_inv += len_subarray2 - 1 # Inversion will occur here as well.
            for m in range(i, len_subarray1):
                A[k] = left_subarray[m]
                k += 1       
        return num_of_inv
    
    def modified_merge_sort(self, A, start, end) -> int:
        """Modified merge sort to return count of inversions.
        Args:
            A: array of integers.
            start: starting index.
            end: last index.
        Returns:
            int
        """
        if start < end:
            mid = (start + end) // 2
            left_count = self.modified_merge_sort(A, start, mid) #getting left subcount
            right_count = self.modified_merge_sort(A, mid + 1, end) #getting right subcount
            return self.modified_merge(A, start, mid, end) + left_count + right_count #combining the result
        return 0

    def num_of_inversions_efficient(self, array) -> int:
        """This algorithm will use modified Merge sort to 
        find all the inversions. runtime O(nlogn).
        Args:
            array: array of integers.
        Returns:
            int.
        """
        return self.modified_merge_sort(array, 0, len(array) - 1)
#Tesing code
inv = InversionInAnArray()
print(inv.num_of_inversions_naive([2, 3, 8, 6, 1, 0]))
print(inv.num_of_inversions_efficient([2, 3, 8, 6, 1, 0]))
print(inv.num_of_inversions_naive([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(inv.num_of_inversions_efficient([1, 2, 3, 4, 5, 6, 7, 8, 9]))