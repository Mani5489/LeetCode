class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        avg = []
        left = 0
        right = len(nums) - 1
        while left < right:
            l = nums[left]
            r = nums[right]
            avg.append((l + r) / 2)
            left += 1
            right -= 1
        return min(avg)