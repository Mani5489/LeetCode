class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        freq = {}
        m = nums[-1]
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        if m != (len(nums)-1):
            return False
        if freq[m] == 2:
            for i, j in freq.items():
                if (i != m) and (j > 1):
                    return False
        else:
            return False
        new = sorted(list(freq.keys()), reverse=True)
        if new[-1] != 1:
            return False
        p = new[0]
        for i in range(1, len(new)):
            n = new[i]
            if (p - n) > 1:
                return False
            p = n
        return True