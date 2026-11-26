class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = sorted(nums[1:])
        return nums[0] + n[0] + n[1]