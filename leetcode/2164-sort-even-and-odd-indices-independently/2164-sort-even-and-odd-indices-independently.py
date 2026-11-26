class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        omap = {}
        emap = {}
        for i, j in enumerate(nums):
            if i % 2 == 0:
                emap[i] = j
            else:
                omap[i] = j
        omap = dict(sorted(omap.items(), key=lambda x: x[1], reverse=True))
        emap = dict(sorted(emap.items(), key=lambda x: x[1]))
        res = []
        for i, j in itertools.zip_longest(list(emap.values()), list(omap.values()), fillvalue=''):
            if i != '':
                res.append(i)
            if j != '':
                res.append(j)
        return res
        