class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        m1 = nums[0]
        m2 = nums[-1]
        nums = [x for x in nums if x!=m1]
        nums = [x for x in nums if x!=m2]
        return len(nums)