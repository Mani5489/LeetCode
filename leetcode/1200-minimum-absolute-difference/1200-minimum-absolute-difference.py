class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        maps = {}
        p = arr[0]
        i = 1
        while i < len(arr):
            n = arr[i]
            d = abs(n - p)
            maps[p, n] = d
            p = n
            i += 1
        m = min(maps.values())
        res = []
        for i, j in maps.items():
            if j == m:
                res.append(list(i))
        return res