class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        maps = {}
        r = 0
        for i in mat:
            s = len([x for x in i if x == 1])
            maps[r] = s
            r += 1
        maps = dict(sorted(maps.items(), key=lambda x: x[1]))
        res = []
        for i, j in maps.items():
            res.append(i)
            k -= 1
            if k == 0:
                break
        return res