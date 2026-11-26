class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tmap = {}
        for i in text:
            tmap[i] = tmap.get(i, 0) + 1
        maps = {}
        for i, j in tmap.items():
            if i in 'balon':
                maps[i] = j
        s = str(tmap.keys())
        if 'a' not in s or 'b' not in s or 'l' not in s or 'o' not in s or 'n' not in s:
            return 0
        t = []
        for i, j in maps.items():
            if i == 'l' or i == 'o':
                t.append(j // 2)
            else:
                t.append(j)
        return min(t)
        