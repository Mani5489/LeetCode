class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ids1 = [x[0] for x in items1]
        ids2 = [x[0] for x in items2]
        cIds = list(set(ids1) & set(ids2))
        ids1 = [x for x in ids1 if x not in cIds]
        ids2 = [x for x in ids2 if x not in cIds]
        res = []
        for i in cIds:
            v1 = sum([x[1] for x in items1 if x[0] == i])
            v2 = sum([x[1] for x in items2 if x[0] == i])
            res.append([i, v1+v2])
        for i in ids1:
            res.extend([x for x in items1 if x[0] == i])
        for i in ids2:
            res.extend([x for x in items2 if x[0] == i])
        return sorted(res)