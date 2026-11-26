class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        new = []
        count = 0
        for i in nums:
            if i > 0:
                new.append(i)
            elif i < 0:
                new.append(i)
            else:
                count += 1
        nums[:] = new
        del new
        for j in range(count):
            nums.append(0)
        
        


        