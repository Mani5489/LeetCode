class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        if len(nums) == 1:
            return 0
        s = float('inf')
        notes = []
        i = 0
        while i <= len(nums) - k:
            sub = nums[i:i + k]
            m1 = sub[0]
            m2 = sub[len(sub) - 1]
            d = m1 - m2
            notes.append(d)
            i += 1
        return min(notes)