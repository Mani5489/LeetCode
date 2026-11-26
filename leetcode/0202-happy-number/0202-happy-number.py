class Solution:
    def isHappy(self, n: int) -> bool:
        s = reduce(lambda x, y: int(x) + int(y), [int(x) * int(x) for x in list(str(n))])
        start = 0
        while s != 1:
            # print(s)
            s = reduce(lambda x, y: int(x) + int(y), [int(x) * int(x) for x in list(str(s))])
            if start > 19:
                return False
            start += 1
        return True
        