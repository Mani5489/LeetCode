class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = max(nums)
        if s < 0:
            return s
        else:
            u = [x for x in list(set(nums)) if x > 0]
            return sum(u)
        