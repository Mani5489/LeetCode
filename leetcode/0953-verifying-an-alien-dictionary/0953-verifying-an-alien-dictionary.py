class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        maps = {}
        i = 1
        for j in order:
            maps[j] = i
            i += 1
        # print(maps)
        k = 0
        res = []
        while k < len(words):
            v = [maps.get(i, 0) for i in words[k]]
            # print(v)
            res.append(v)
            k += 1
        p = res[0]
        for i in range(1, len(res)):
            n = res[i]
            if p > n:
                return False
            p = n
        return True