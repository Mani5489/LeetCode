class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        rs = ''
        for i in s:
            if i.isalnum():
                rs = rs + i
        rss = rs[::-1]
        # print(rs)
        # print(rss)
        if s is None or s == "":
            return True
        return rs == rss

        