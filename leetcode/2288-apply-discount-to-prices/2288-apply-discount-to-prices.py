class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for index, word in enumerate(words):
            if word.startswith('$') and len(word) > 1 and word[1:].isdigit():
                price = float(word[1:])
                new_price = price * (1 - (discount / 100))
                words[index] = f"${round(new_price, 2):.2f}"
        return " ".join(words)
        