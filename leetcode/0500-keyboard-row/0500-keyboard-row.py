class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = list('qwertyuiop')
        set2 = list('asdfghjkl')
        set3 = list('zxcvbnm')
        res = []
        for word in words:
            maps = list(set(word))
            if all(x.lower() in set1 for x in maps) or all(x.lower() in set2 for x in maps) or all(x.lower() in set3 for x in maps):
                res.append(word)
        return res