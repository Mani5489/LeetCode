class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counts = Counter(words[0])
        # print(common_counts)
        for word in words[1:]:
            word_counts = Counter(word)
            # print(word_counts)
            for char in common_counts:
                common_counts[char] = min(word_counts[char], common_counts[char])
        # print(common_counts)
        res = []
        for char, count in common_counts.items():
            res.extend([char] * count)
        return res
        