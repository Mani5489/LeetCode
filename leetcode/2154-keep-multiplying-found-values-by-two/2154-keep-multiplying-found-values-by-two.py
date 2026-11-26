class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == original:
                return Solution().findFinalValue(nums, original * 2)
            elif nums[mid] > original:
                high = mid - 1
            else:
                low = mid + 1
        return original
