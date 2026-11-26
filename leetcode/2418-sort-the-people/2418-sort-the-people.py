class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maps = {}
        for i, j in zip(heights, names):
            maps[i] = j
        maps = dict(sorted(maps.items(), key=lambda x: x[0],reverse=True))
        return list(maps.values())