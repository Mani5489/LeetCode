class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c = 0
        t = list(text.split(' '))
        for i in t:
            s = list(set(i))
            b = any(j in brokenLetters for j in s)
            if b is False:
                c += 1
        return c