class Solution:
    def finalString(self, s: str) -> str:
        faulty = []
        for i in s:
            if i.lower() == 'i':
                faulty[:] = faulty[::-1]
            else:
                faulty.append(i)
        return ''.join(faulty)
        