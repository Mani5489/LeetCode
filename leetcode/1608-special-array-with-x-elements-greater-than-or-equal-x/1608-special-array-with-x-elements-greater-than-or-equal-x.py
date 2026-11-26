class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):
            count = 0
            for j in range(0, len(nums)):
                if nums[j] >= i:
                    count += 1
            if count == i:
                return i
        return -1
        