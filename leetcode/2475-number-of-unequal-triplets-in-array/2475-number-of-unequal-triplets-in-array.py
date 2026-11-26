class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        left = 0
        right = len(nums)
        answer = 0
        for c in list(freq.values()):
            right -= c
            answer += left * c * right
            left += c
        return answer