class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listOfWords = s.split()
        if len(pattern) != len(listOfWords):
            return False
        char_to_word = {}
        word_to_char = {}
        for char, word in zip(pattern, listOfWords):
            if char in char_to_word and char_to_word[char] != word:
                return False
            if word in word_to_char and word_to_char[word] != char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char
        return True
        