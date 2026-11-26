class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        p = []
        i = 0
        while i < len(s):
            if s[i] != goal[i]:
                p.append(i)
            i += 1
        n = len(p)
        if n > 2:
            return False
        elif n == 2:
            left, right = p[0], p[1]
            s = list(s)
            s[left], s[right] = s[right], s[left]
            s = "".join(s)
            return s == goal
        elif n == 0:
            return len(set(s)) < len(s)
        return False