class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        # print(freq)
        v1 = list(freq.values())
        v2 = list(set(v1))
        if len(v1) == len(v2):
            return True
        else:
            return False