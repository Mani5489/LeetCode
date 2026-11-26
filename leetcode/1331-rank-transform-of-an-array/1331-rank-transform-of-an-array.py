class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = sorted(list(set(arr)))
        r = 1
        ranks = {}
        for i in n:
            ranks[i] = r
            r += 1
        res = []
        for i in arr:
            getRank = ranks.get(i)
            res.append(getRank)
        return res