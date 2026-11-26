class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maps = {}
        new = sorted(nums)
        for i in range(len(new)):
            keys = maps.keys()
            if new[i] not in keys:
                maps[new[i]] = i
        res = []
        for i in nums:
            res.append(maps.get(i))
        return res