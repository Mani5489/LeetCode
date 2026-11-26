class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        freq = {k: v for k, v in freq.items() if v == 1}
        return sum(freq.keys())