class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'v': 0, 'u': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        for i in sentence:
            v = freq.get(i, 0)
            if v == 0:
                freq[i] = 1
            elif v > 1:
                continue
        return True if (sum(freq.values()) >= 26) else False