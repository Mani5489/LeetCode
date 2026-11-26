class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sums = 0
        c = 0
        tt = sum(arr) // 3
        if sum(arr) % 3 != 0:
            return False
        # print(tt)
        for i in range(len(arr)):
            sums += arr[i]
            if sums == tt:
                if c > 2 and i < len(arr):
                    return True
                c += 1
                sums = 0
        #     print(sums)
        # print(c, tt)
        return c > 2
        