class Solution:
    def findLucky(self, arr: list[int]) -> int:
        maps = {}
        for i in arr:
            maps[i] = maps.get(i, 0) + 1
        maps = dict(sorted(maps.items(), key=lambda x: x[1],reverse=True))
        for i, j in maps.items():
            if i == j:
                return i
        return -1