class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        factor = [2, 3, 5]
        for i in factor:
            while n % i == 0:
                n = n // i
        if n == 1:
            return True
        else:
            return False
        