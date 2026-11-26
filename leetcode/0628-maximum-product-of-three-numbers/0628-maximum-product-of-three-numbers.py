class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        comb_1 = nums[0] * nums[1] * nums[len(nums) - 1]
        comb_2 = nums[-1] * nums[-2] * nums[-3]
        return max(comb_1, comb_2)

        