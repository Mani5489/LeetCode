class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # task 1
        seq = [nums[0]]
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                seq.append(nums[i])
                prev = nums[i]
            else:
                break
        total = sum(seq)
        # task 2
        num_set = set(nums)
        while total in num_set:
            total += 1
        return total