class PowerFactorial(object):
    """ Calculates X^Y and X! using
        iterative and recursive algorithms.
    """
    def power_loop(self, x, y) -> int:
        """Calculates X^Y using iterative technique.
        Args:
            X: int
            Y: int greater than 0
        Returns: int
        """
        ans = 1
        for i in range(y):
            ans *= x
        return ans
    
    def power_recursion(self, x, y) -> int:
        """Calculates X^Y using recursive technique.
        Args:
            X: int
            Y: int greater than 0
        Returns: int
        """
        if y == 1:
            return x
        return x * self.power_recursion(x, y - 1)
    
    def factorial_loop(self, number) -> int:
        """Calculates X! using iterative technique.
        Args:
            X: int
        Returns: int
        """
        if number == 0 or number == 1 or number == 2:
            return number
        else:
            ans = 2
            for i in range(3, number + 1):
                ans *= i
            return ans
    
    def factorial_recursion(self, number) -> int:
        """Calculates X! using recursive technique.
        Args:
            X: int
        Returns: int
        """
        if number == 0 or number == 1 or number == 2:
            return number
        else:
            return number * self.factorial_recursion(number - 1)

pf = PowerFactorial()
print(pf.power_loop(10, 0))
print(pf.power_recursion(10, 5))
print(pf.factorial_loop(1))
print(pf.factorial_recursion(10))
