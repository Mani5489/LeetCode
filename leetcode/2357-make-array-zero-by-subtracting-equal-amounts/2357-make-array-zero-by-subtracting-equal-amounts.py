class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        seen = set()
        for i in nums:
            if i != 0:
                seen.add(i)
        return len(seen)
        