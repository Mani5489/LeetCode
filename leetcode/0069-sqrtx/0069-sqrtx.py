class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            # print(mid)
            # print(mid * mid)
            if (mid * mid) == x:
                return mid
            elif (mid * mid) > x:
                high = mid - 1
            else:
                low = mid + 1
        return min(low, high)
        