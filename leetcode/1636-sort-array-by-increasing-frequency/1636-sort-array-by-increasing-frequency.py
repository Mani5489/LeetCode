class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        freq = dict(sorted(freq.items(), key=lambda x: (x[1], -x[0])))
        res = []
        for i, j in freq.items():
            while j > 0:
                res.append(i)
                j -= 1
        return res