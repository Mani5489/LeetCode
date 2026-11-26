class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maps = {}
        res = []
        for i in arr1:
            maps[i] = maps.get(i, 0) + 1
        for i in arr2:
            j = maps.get(i)
            while j > 0:
                res.append(i)
                j -= 1
        left = [x for x in arr1 if x not in arr2]
        left.sort()
        return res + left