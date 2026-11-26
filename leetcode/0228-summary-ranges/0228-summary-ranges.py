class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            # Find the end of the current range by checking the next index
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            # If the pointer moved, it's a range; otherwise, it's a single number
            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")
            else:
                result.append(f"{start}")

            i += 1  # Move to the start of the next potential range
        return result
        