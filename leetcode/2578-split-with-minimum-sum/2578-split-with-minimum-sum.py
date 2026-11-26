class Solution:
    def splitNum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        n1, n2 = '', ''
        i, j = 0, 1
        while i < len(num):
            n1 += num[i]
            i += 2
        while j < len(num):
            n2 += num[j]
            j += 2
        return int(n1)+int(n2)
        