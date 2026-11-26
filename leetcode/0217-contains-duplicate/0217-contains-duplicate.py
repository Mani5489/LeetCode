class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsCopy = set(nums)
        if len(numsCopy) == len(nums):
            return False
        else:
            return True
        