class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            price = n - (n - 1)
            flowerbed[0] = price
            n = n - price
        i = 0
        while 0 <= i <= len(flowerbed) - 1:
            if i - 1 < 0:
                i = 0
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    price = n - (n - 1)
                    flowerbed[i] = price
                    n = n - price
                i += 1
            elif i + 1 > len(flowerbed) - 1:
                i = len(flowerbed) - 1
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    price = n - (n - 1)
                    flowerbed[i] = price
                    n = n - price
                i += 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    price = n - (n - 1)
                    flowerbed[i] = price
                    n = n - price
                i += 1
        return n <= 0