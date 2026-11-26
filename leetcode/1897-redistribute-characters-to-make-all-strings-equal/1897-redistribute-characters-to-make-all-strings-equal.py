class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        f = Counter()
        for word in words:
            f.update(word)
        # print(f)
        n = len(words)
        for i, j in f.items():
            if j % n != 0:
                return False
        return True