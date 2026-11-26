class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        # print(freq)
        maxOdd = 0
        for i in freq.values():
            if i % 2 != 0:
                if maxOdd < i:
                    maxOdd = i
        # print(maxOdd)
        longest = 0
        for i in freq.values():
            if i % 2 == 0:
                longest += i
            else:
                longest += (i - 1)
        if maxOdd in freq.values():
            return longest + 1
        return longest
        