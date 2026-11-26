class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for sub in range(n // 2, 0, -1):
            # Candidate length must divide the total length
            if n % sub != 0:
                continue
            substring = s[:sub]
            repeat = n // sub
            if substring * repeat == s:
                return True
        return False



        