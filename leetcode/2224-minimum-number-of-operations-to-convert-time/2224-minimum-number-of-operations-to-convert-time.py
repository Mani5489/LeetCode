class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.replace(':', '')
        chh, cmm = int(current[0:2]), int(current[2:4])
        correct = correct.replace(':', '')
        ehh, emm = int(correct[0:2]), int(correct[2:4])
        operations = [15, 5, 1]
        hd = (ehh - chh) * 60
        sd = (emm - cmm)
        t1 = (hd + sd)
        t2 = ((hd + sd) // 60) * 60
        r = t1 - t2
        i = 0
        o = (hd + sd) // 60
        while i < len(operations):
            new, c = divmod(r, operations[i])
            r = c
            o += new
            i += 1
        return o