class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number = list(number)
        c = []
        m = ''
        for i in range(len(number)):
            if number[i] == digit:
                c.append(i)
        i = 0
        while i < len(c):
            cp = number.copy()
            ind = c[i]
            cp.pop(ind)
            s = ''.join(cp)
            if s > m:
                m = s
            i += 1
        return m
        