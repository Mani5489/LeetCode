class Solution:
    def distMoney(self, money: int, children: int) -> int:
        mm = {}
        i = 0
        while i < children:
            mm[i] = 1
            money -= 1
            i += 1
        # print(money, mm)
        if money == 0:
            return 0
        elif money < 0:
            return -1
        for i, j in mm.items():
            if money > 7:
                make = j + 7
                money -= 7
                mm[i] = make
            else:
                mm[i] = j + money
                money -= money
        # print(money, mm)
        if money > 0:
            r = mm[len(mm) - 1]
            mm[len(mm) - 1] = r + money
            money -= money
        # print(money, mm)
        fs = [x for x, y in mm.items() if y == 4]
        if not fs:
            return len([x for x, y in mm.items() if y == 8])
        elif fs:
            c = fs[0]
            if c + 1 < len(mm):
                p = c + 1
            else:
                p = c - 1
            cv = mm[c]
            cp = mm[p]
            mm[c] = cv - 1
            mm[p] = cp + 1
        # print(money, mm)
        return len([x for x, y in mm.items() if y == 8])