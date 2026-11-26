class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # if n<=1: return s
        palind = ''

        for i in range(n-1):
            if s[i] == s[i+1]:
                l, r = i-1, i+2
                while l>=0 and r<n and s[l] == s[r]:
                    l-=1
                    r+=1
                new = s[l+1: r]
                # print(new)
                if len(new) > len(palind):
                    palind = new
            if i<(n-2) and s[i] == s[i+2]:
                l, r = i-1, i+3
                while l>=0 and r<n and s[l] == s[r]:
                    l-=1
                    r+=1
                new = s[l+1: r]
                # print(new)
                if len(new) > len(palind):
                    palind = new
        # print(palind)
        if palind: return palind
        return s[0]