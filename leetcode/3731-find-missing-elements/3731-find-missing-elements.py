class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        left = []
        for i in range(nums[0], nums[-1]):
            if i not in nums:
                left.append(i)
        return left