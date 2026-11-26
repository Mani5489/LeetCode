class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        leftover = []
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] % 2 == 0:
                res.append(nums[i])
            else:
                leftover.append(nums[i])
            i += 1
        return res + leftover