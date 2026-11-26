class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = "".join(map(str, digits))
        s = int(s) + 1
        results = []
        for i in str(s):
            results.append(int(i))
        return results
        