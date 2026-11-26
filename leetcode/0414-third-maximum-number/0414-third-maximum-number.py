class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(dict.fromkeys(nums)), reverse=True)
        try:
            return nums[2]
        except IndexError:
            return max(nums, default=0)
