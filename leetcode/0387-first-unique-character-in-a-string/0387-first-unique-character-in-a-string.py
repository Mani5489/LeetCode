class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps = {}
        for i in s:
            maps[i] = maps.get(i,0)+1
        for i in maps.keys():
            if maps[i] == 1:
                return s.index(i)
        return -1
