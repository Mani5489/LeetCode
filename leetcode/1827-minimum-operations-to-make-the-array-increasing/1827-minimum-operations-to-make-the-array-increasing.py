class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        prev = nums[0]
        operations = 0
        for i in range(1, len(nums)):
            val = nums[i]
            if val <= prev:
                diff = (prev - val) + 1
                val += diff
                operations += diff
            nums[i] = val
            prev = nums[i]
        return operations
        