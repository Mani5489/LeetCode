class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        s = []
        for i in dominoes:
            s.append((min(i), max(i)))
        maps = {}
        for i in s:
            maps[i] = maps.get(i, 0) + 1
        print(maps)
        ans = 0
        for f in maps.values():
            ans += f * (f - 1) // 2
        return ans