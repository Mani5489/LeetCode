class Solution:
    def largestInteger(self, num: int) -> int:
        o = {x: y for x, y in enumerate(list(str(num))) if int(y) % 2 != 0}
        e = {x: y for x, y in enumerate(list(str(num))) if int(y) % 2 == 0}
        okeys = list(o.keys())
        ovalues = sorted(o.values(), reverse=True)
        o = dict(zip(okeys, ovalues))
        ekeys = list(e.keys())
        evalues = sorted(e.values(), reverse=True)
        e = dict(zip(ekeys, evalues))
        m = e | o
        m = dict(sorted(m.items(), key=lambda x: x[0]))
        return int(''.join(list(m.values())))