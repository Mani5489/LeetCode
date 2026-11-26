class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = maps.get(nums[i], 0) + 1
        p = 0
        for n in maps.values():
            p += (n * (n - 1)) // 2
        return p