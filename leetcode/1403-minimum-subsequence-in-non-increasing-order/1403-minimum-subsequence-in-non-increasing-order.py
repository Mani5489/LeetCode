class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        rsort = sorted(nums, reverse=True)
        rem = sum(nums)
        pick = 0
        i = 0
        res = []
        while rem >= pick:
            pick += rsort[i]
            rem -= rsort[i]
            res.append(rsort[i])
            i += 1
        return res
        