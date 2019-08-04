class GCD(object):
    """Greates common diviser calculator.
    """
    def euclid_gcd(self, a, b) -> int:
        """Calculate GCD using Euclid method.
        Args:
            a: first number.
            b: Second number.
        Returns:
            int: GCD of a and b.
        """
        while b != 0:
            a = a % b
            a, b = b, a
        return a
gcd = GCD()
print(gcd.euclid_gcd(60, 96))
print(gcd.euclid_gcd(20, 8))