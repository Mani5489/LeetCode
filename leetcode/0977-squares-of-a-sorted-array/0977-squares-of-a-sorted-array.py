class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted([x*x for x in nums])
        return nums
        