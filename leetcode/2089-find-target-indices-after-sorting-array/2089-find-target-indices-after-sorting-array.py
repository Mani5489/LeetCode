class Solution:
    def leftsearch(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        # print(first)
        return first

    def rightsearch(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        # print(first)
        return first

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = Solution.leftsearch(self, nums, target)
        right = Solution.rightsearch(self, nums, target)

        if left == -1: return []

        return list(range(left, right + 1))