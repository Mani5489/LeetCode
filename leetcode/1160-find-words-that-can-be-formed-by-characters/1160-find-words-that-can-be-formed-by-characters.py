class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounts = {}
        for char in chars:
            charCounts[char] = charCounts.get(char, 0) + 1
        total_len = 0
        for word in words:
            # Check if we have enough of each letter for THIS specific word
            # word.count(c) ensures we don't exceed the available quantity
            if all(word.count(c) <= charCounts.get(c, 0) for c in set(word)):
                total_len += len(word)
        return total_len

        