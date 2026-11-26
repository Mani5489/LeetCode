class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1
        for x, y in hash.items():
            if y > 1:
                return x
        