class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        maps = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
                 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
                 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
                 'y': "-.--", 'z': "--.."}
        res = {}
        for word in words:
            code = "".join([maps[x] for x in word])
            res[code] = word
        return len(res.keys())