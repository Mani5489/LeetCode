class Solution:
    def minTimeToType(self, word: str) -> int:
        maps1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                 "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
                 "x": 24, "y": 25, "z": 26}
        p = 'a'
        mt = 0
        w = 0
        for t in word:
            if t == 'a':
                pass
            cc = abs(maps1.get(t) - maps1.get(p))
            ac = abs(26 - cc)
            # print(cc, ac)
            mt += min(cc, ac)
            p = t
            w += 1
        return mt + w
