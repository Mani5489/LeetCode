class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        p1, p2 = nums[len(nums) - 1], nums[len(nums) - 2]
        p3, p4 = nums[0], nums[1]
        return (p1 * p2) - (p3 * p4)