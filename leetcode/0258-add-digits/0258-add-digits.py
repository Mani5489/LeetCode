class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            if num % 9 == 0:
                num = 9
            else:
                num = num % 9
        return num


        