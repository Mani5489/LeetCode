class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(0, len(nums) - 2):
            x, y, z = nums[i], nums[i + 1], nums[i + 2]
            if x + y > z and y + z > x and x + z > y:
                return x + y + z
        return 0
        