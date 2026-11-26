class Solution:
    def minimumPushes(self, word: str) -> int:
        r, q = divmod(len(word), 8)
        t = 0
        for i in range(1, r + 1):
            t += i * 8
        t += q * (r + 1)
        return t

        