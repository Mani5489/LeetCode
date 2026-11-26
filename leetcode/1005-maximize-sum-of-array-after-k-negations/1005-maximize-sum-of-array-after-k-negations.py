class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < k:
            nums.sort()
            m = nums[0]
            m = m * (-1)
            nums[0] = m
            i += 1
        return sum(nums)