class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[: k])
        maxSum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > maxSum:
                maxSum = current_sum
        return maxSum / k
        