class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 1
        for item in nums[:]:
            if item == val:
                nums.remove(item)
            else:
                count += 1
        return count
         