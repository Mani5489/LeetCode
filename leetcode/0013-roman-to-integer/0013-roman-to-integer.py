class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        KeysValues = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        if not all(c in KeysValues for c in s):
            return 0
        i = 0
        total = 0
        while i < len(s):
            if i + 1 < len(s) and KeysValues[s[i]] < KeysValues[s[i + 1]]:
                total += KeysValues[s[i + 1]] - KeysValues[s[i]]
                i += 2
            else:
                total += KeysValues[s[i]]
                i += 1
        return total

