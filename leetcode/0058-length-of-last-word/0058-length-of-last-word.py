class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        list1 = list(s.split(" "))
        # results = []
        # for i in list1:
        #     if i:
        #         results.append(i)
        length = len(list1[-1])
        return length
        