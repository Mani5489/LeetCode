class Solution:
    def sortSentence(self, s: str) -> str:
        maps = {}
        for i in list(s.split()):
            val, key = i[:len(i) - 1], i[len(i) - 1:]
            maps[key] = val
        maps = dict(sorted(maps.items(), key=lambda x: x[0]))
        return ' '.join(maps.values())