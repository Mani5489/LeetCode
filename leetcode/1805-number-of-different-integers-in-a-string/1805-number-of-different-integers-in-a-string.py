class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nword = ''
        for i in word:
            if i.isdigit():
                nword += i
            else:
                nword += ','
        n = list(nword.split(','))
        new = set()
        for i in n:
            if i != '':
                new.add(int(i))
        return len(new)