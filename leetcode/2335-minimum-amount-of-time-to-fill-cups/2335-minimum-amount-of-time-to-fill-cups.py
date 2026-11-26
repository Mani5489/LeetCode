class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        s = 0
        c, w, h = amount[0], amount[1], amount[2]
        if c > 0 and w == 0 and h == 0:
            return c
        elif c == 0 and w == 0 and h == 0:
            return 0
        i = 0
        while sum(amount) > 0:
            # print(amount)
            amount.sort(reverse=True)
            p, n = amount[0], amount[1]
            if p > 0 and n > 0:
                p = p - 1
                n = n - 1
                amount[0], amount[1] = p, n
            elif p > 0 and n == 0:
                p = p - 1
                amount[0] = p
            s += 1
            i += 1
        return s