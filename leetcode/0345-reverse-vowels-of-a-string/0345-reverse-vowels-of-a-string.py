class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        collect = []
        for i in s:
            if i.lower() in vowels:
                collect.append(i)
        collect[:] = collect[::-1]
        i = 0
        res = ''
        for index, char in enumerate(s):
            if char.lower() in vowels:
                res += collect[i]
                i += 1
            else:
                res += char
        return res
        