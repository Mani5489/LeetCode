class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maps = {}
        for i in nums:
            if i > 0:
                j = i * (-1)
                if j in nums:
                    maps[i] = j
        maps = dict(sorted(maps.items(), key=lambda x: x[0], reverse=True))
        return list(maps.keys())[0] if maps else -1
        