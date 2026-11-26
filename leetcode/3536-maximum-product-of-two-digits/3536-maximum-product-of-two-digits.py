class Solution:
    def maxProduct(self, n: int) -> int:
        nums = list(map(int,str(n)))
        nums.sort(reverse=True)
        return nums[0]*nums[1]