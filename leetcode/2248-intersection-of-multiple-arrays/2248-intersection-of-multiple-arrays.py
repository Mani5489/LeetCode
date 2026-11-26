class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        p = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            p = list(set(p) & set(n))
        return sorted(p)