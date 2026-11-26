class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degrees = sorted(Counter(nums).items(), key=lambda x: x[1])
        m = max(degrees, key=lambda x: x[1])[1]
        degrees = list(filter(lambda x: x[1] == m, degrees))
        s = float('inf')
        first = {}
        for i in nums:
            first[i] = nums.index(i)
        last = {}
        new = nums[::-1]
        for i in nums:
            last[i] = len(nums) - 1 - new.index(i)
        for i in degrees:
            n = i[0]
            f = first[n]
            l = last[n]
            c = l - f + 1
            if c < s:
                s = c
        return s