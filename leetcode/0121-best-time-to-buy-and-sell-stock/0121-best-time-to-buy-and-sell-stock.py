class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Start with the highest possible number
        max_profit = 0            # Start with no profit
        
        for price in prices:
            # 1. Update the lowest buying price seen so far
            if price < min_price:
                min_price = price
            # 2. Check if selling today beats our best profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
        