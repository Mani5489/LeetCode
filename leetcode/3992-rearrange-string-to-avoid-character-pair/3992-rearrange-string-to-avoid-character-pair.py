class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        maps = {}
        for i in s:
            maps[i] = maps.get(i, 0) + 1
        if y not in s or x not in s:
            return s
        else:
            cx = maps[x]
            cy = maps[y]
            t = y * cy + x * cx
        for i in s:
            if i not in t:
                m = maps[i]
                t = i*m + t
        return t