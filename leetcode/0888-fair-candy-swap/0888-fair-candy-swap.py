class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        total = sum_alice + sum(bobSizes)
        target = total // 2
        delta = target - sum_alice

        bob_set = set(bobSizes)

        for alice_box in aliceSizes:
            needed_bob_box = alice_box + delta

            if needed_bob_box in bob_set:
                return [alice_box, needed_bob_box]