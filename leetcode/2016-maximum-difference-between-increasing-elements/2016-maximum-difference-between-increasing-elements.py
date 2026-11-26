class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_diff = float('inf')
        max_diff = 0
        for num in nums:
            if num < min_diff:
                min_diff = num
            elif num - min_diff > max_diff:
                max_diff = num - min_diff
        return -1 if max_diff == 0 else max_diff
        