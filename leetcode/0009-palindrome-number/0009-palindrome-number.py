class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == '':
            return False
        stringX = str(x)
        return stringX == stringX[::-1]

        