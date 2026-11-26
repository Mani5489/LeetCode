class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        p = sorted(words[0])
        copy1 = copy.deepcopy(words)
        i = 1
        while i < len(words):
            word = words[i]
            n = sorted(word)
            if p == n:
                copy1.pop(copy1.index(word))
            else:
                p = n
            i += 1
        return copy1
        