class Solution:
    def myAtoi(self, s: str) -> int:
        min_val = -2 ** 31
        max_val = 2 ** 31 - 1

        def checkRange(num: int) -> int:
            if num < min_val:
                return min_val
            elif num > max_val:
                return max_val
            else:
                return num

        def toNum(s: str, i: int) -> int:
            results = []
            while i < len(s) and s[i].isdigit():
                results.append(s[i])
                i += 1
            return int(''.join(results)) if results else 0

        s = s.strip()
        if not s:
            return 0

        i = 0
        Neg = 1

        if s[i] == '-':
            i += 1
            Neg = -1
        elif s[i] == '+':
            i += 1

        if i >= len(s) or not s[i].isdigit():
            return 0

        value = toNum(s, i)
        value = Neg * value
        return checkRange(value)