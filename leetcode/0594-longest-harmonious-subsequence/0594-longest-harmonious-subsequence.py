class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maps = {}
        for i in nums:
            maps[i] = maps.get(i, 0) + 1
        maps = dict(sorted(maps.items()))
        print(maps)
        mykeys = list(maps.keys())
        m = 0
        p = mykeys[0]
        for i in range(1, len(mykeys)):
            n = mykeys[i]
            v1, v2 = maps.get(p, 0), maps.get(n, 0)
            if n - p == 1:
                s = v1 + v2
                if m < s:
                    m = s
            p = n
        return m
        