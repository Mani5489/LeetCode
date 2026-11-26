class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ss = sorted(score, reverse=True)
        c = score.copy()
        if len(score) < 2:
            return ["Gold Medal"]
        if len(score) < 3:
            r1, r2 = score[0], score[1]
            if r1 < r2:
                return ["Silver Medal", "Gold Medal"]
            else:
                return ["Gold Medal", "Silver Medal"]
        r1, r2, r3 = ss[0], ss[1], ss[2]
        for i in range(len(c)):
            if r1 == ss[i]:
                ind1 = c.index(r1)
                c[ind1] = "Gold Medal"
            elif r2 == ss[i]:
                ind2 = c.index(r2)
                c[ind2] = "Silver Medal"
            elif r3 == ss[i]:
                ind3 = c.index(r3)
                c[ind3] = "Bronze Medal"
        i = 0
        while i < len(c):
            if isinstance(c[i], int):
                ind = ss.index(c[i])
                c[i] = str(ind + 1)
            i += 1
        return c
        