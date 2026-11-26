class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        maps = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,'j': 9, 'k': 10, 'l': 11, 'm': 12,
                'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
                'y': 24, 'z': 25}
        s = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                v1 = maps.get(s[l])
                v2 = maps.get(s[r])
                low = min(v1, v2)
                getK = [k for k, v in maps.items() if v == low]
                # print(getK)
                # print(v1, v2, low)
                s[r] = getK[0]
                if v1 < v2:
                    s[r] = getK[0]
                else:
                    s[l] = getK[0]
            l += 1
            r -= 1
        return ''.join(s)
        