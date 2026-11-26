class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        c1, c2 = prices[0], prices[1]
        if (c1 + c2) > money:
            return money
        else:
            return money - (c1 + c2)
        