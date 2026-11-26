class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            # Use the math formula to find total coins needed for 'mid' rows
            coins_needed = (mid * (mid + 1)) // 2

            if coins_needed == n:
                return mid
            elif coins_needed < n:
                low = mid + 1
            else:
                high = mid - 1

        # 'high' will end up at the largest number of full rows
        return high