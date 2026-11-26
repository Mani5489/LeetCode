class Solution:
    def sortString(self, s: str) -> str:
        o1 = 'abcdefghijklmnopqrstuvwxyz'
        o2 = o1[::-1]
        maps1 = {}
        for i in s:
            maps1[i] = maps1.get(i, 0) + 1
        res = ''
        while sum(maps1.values()) > 0:
            for c in o1:
                if c in maps1.keys() and maps1[c] > 0:
                    v = maps1[c]
                    maps1[c] = v-1
                    res += c
            for c in o2:
                if c in maps1.keys() and maps1[c] > 0:
                    v = maps1[c]
                    maps1[c] = v-1
                    res += c
        return res
        