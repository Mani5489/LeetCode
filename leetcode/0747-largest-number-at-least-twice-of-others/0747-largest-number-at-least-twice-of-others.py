class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l = max(nums)
        for i in nums:
            if i == l or i == 0:
                pass
            elif l < 2 * i:
                return -1
        return nums.index(l)
        