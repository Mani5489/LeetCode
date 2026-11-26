class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s = 0
        nums.sort(reverse=True)
        while k > 0:
            l = nums[0]
            s += l
            l += 1
            nums[0] = l
            k -= 1
        return s