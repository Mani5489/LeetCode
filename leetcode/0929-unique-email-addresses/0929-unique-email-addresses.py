class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        s = set()
        for i in emails:
            left, right = i.split("@")
            left = left.replace(".", "")
            if '+' in left:
                index = left.index('+')
                left = left[:index]
            f = left + '@' + right
            s.add(f)
        return len(s)