class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        f = {}
        for i in deck:
            f[i] = f.get(i, 0) + 1
        v = [y for x, y in f.items()]
        x = 2
        m = min(v)
        while x <= m:
            if all(y % x == 0 for y in f.values()):
                return True
            x += 1
        return False