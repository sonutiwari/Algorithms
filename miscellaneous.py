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
misc = Miscellaneous()
print(misc.add_binary([1, 1, 1], [1, 1, 1]))
            