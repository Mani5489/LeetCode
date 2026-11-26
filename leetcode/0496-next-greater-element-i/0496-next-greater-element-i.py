class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                pop_num = stack.pop()
                next[pop_num] = num
            stack.append(num)
        return [next.get(num, -1) for num in nums1]
        