class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        avg = []
        while left < right:
            r1 = nums[left]
            r2 = nums[right]
            avg.append((r1 + r2) / 2)
            left += 1
            right -= 1
        return len(list(set(avg)))