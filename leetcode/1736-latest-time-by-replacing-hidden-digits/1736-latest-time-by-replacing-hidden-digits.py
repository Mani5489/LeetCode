class Solution:
    def hhformated(self, hh, choice1, choice2) -> str:
        i = 0
        prev = 0
        ind = 0
        while i < len(hh):
            if hh[i] == '?' and i == 0:
                hh[i] = str(choice1)
                prev = hh[i]
                ind = i
            elif hh[i] == '?' and i == 1:
                if prev == 2:
                    hh[i] = str(3)
                else:
                    hh[i] = str(choice2)
                ind = i
            i += 1
        hint = int(''.join(hh))
        while hint > 23:
            if ind == 0:
                hh[ind] = str(choice1)
                hint = int(''.join(hh))
                choice1 -= 1
            else:
                hh[ind] = str(choice2)
                hint = int(''.join(hh))
                choice2 -= 1
        return "".join(hh)

    def mmformated(self, hh, choice1, choice2) -> str:
        i = 0
        prev = 0
        ind = 0
        while i < len(hh):
            if hh[i] == '?' and i == 0:
                hh[i] = str(choice1)
                prev = hh[i]
                ind = i
            elif hh[i] == '?' and i == 1:
                if prev == 5:
                    hh[i] = str(9)
                else:
                    hh[i] = str(choice2)
                ind = i
            i += 1
        hint = int(''.join(hh))
        while hint > 59:
            if ind == 0:
                hh[ind] = str(choice1)
                hint = int(''.join(hh))
                choice1 -= 1
            else:
                hh[ind] = str(choice2)
                hint = int(''.join(hh))
                choice2 -= 1
        return "".join(hh)

    def maximumTime(self, time: str) -> str:
        nums = time.replace(':', '')
        hh = self.hhformated(list(nums[0:2]), 2, 9)
        mm = self.mmformated(list(nums[2:4]), 5, 9)
        return hh + ":" + mm