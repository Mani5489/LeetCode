class Solution:
    def maximum69Number (self, num: int) -> int:
        maps = {6: 9, 9: 6}
        combs = []
        i = 0
        while i < len(str(num)):
            s = list(str(num))
            g = maps.get(int(s[i]), 0)
            s[i] = str(g)
            combs.append(reduce(lambda x, y: x + y, s))
            i += 1
        combs.append(num)
        return max(map(int, combs))
        