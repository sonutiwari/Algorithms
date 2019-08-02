""" All uncategorized algorithms will reside here. """
class Miscellaneous(object):
    def add_binary(self, first_num, second_num):
        """ Add two binary arrays and gives result.
        Args:
            first_num: binary array of first number.
            second_num: binary array of second number.
        Returns:
            ans: Binary result of adding first number to second number.
        """
        ans = []
        temp = zip(reversed(first_num), reversed(second_num))
        res = 0
        for (i, j) in temp:
            ans.append((res + i + j) % 2)
            res = (res + i + j) // 2
        if res == 1:
            ans.append(res)
        return ans[::-1]

    def sum_subset(self, array, X):
        """To find if two numbers exist in array whose sum is equal to number X
            Args:
            array : the array of integers.
            X: The sum.

            Returns:
                True if some exists.
                False otherwise.
        """
        array.sort()
        left_pointer = 0
        right_pointer = len(array) - 1
        while(left_pointer < right_pointer):
            temp = array[left_pointer] + array[right_pointer]
            if temp == X:
                return True
            elif temp > X:
                right_pointer -= 1
            else:
                left_pointer += 1
        return False    
misc = Miscellaneous()
print(misc.add_binary([1, 1, 1], [1, 1, 1]))
print(misc.sum_subset([1, 2, 5, 4, 3, 7, 6, 9, 8], 10))
print(misc.sum_subset([1, 2, 5, 4, 3, 7, 6, 9, 8], 20))
            