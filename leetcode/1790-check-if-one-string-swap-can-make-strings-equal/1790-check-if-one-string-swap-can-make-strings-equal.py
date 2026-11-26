class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        map1 = dict(Counter(s1))
        map2 = dict(Counter(s2))
        for i, j in zip(sorted(list(map1.keys())), list(sorted(map2.keys()))):
            c1 = map1.get(i)
            c2 = map2.get(j)
            if (i != j) and (c1 != c2):
                return False
        ind1 = {}
        for i in range(len(s1)):
            ind1[i] = s1[i]
        ind2 = {}
        for i in range(len(s1)):
            ind2[i] = s2[i]
        records = []
        for i in range(len(s1)):
            k = ind1.get(i)
            l = ind2.get(i)
            if k != l:
                records.append(i)
        s1 = list(s1)
        s2 = list(s2)
        if len(records) == 2:
            s2[records[0]], s2[records[1]] = s2[records[1]], s2[records[0]]
            if s1 == s2:
                return True
        return False