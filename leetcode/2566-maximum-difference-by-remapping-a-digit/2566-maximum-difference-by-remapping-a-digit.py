class Solution:
    def minMaxDifference(self, num: int) -> int:
        if all(x == '9' for x in list(str(num))):
            return num
        if num == 0:
            return num
        snum = str(num)
        mm = 0
        mi = 0
        for i in snum:
            if i != '9':
                mm = snum.replace(i, '9')
                break
        for i in snum:
            if i != '0':
                mi = snum.replace(i, '0')
                break
        # print(mm, mi)
        return int(mm) - int(mi)
        