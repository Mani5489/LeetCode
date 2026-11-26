class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1 + " " + s2
        f = {}
        for i in list(words.split()):
            f[i] = f.get(i, 0) + 1
        f = [x for x, y in f.items() if y == 1]
        return f