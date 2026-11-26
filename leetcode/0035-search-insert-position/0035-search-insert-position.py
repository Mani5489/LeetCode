class Solution(object):
    def searchInsert(self, nums, target):
        value = 0
        for index, char in enumerate(nums):
            if char == target:
                value = index
                break
            elif not char < target:
                value = index
                break
            elif target not in nums and target > nums[len(nums) - 1]:
                value = len(nums)
                break
        return value


        