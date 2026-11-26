class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]
        if ((a + b) > c) & ((b + c) > a) & ((c + a) > b):
            if a == b == c:
                return 'equilateral'
            elif a != b != c != a:
                return 'scalene'
            else:
                return 'isosceles'
        else:
            return 'none'