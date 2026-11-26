class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced_count = 0

        # We cannot sort baskets globally because the problem requires
        # finding the "leftmost available basket" in its original position.
        for fruit in fruits:
            matched = False
            for i in range(len(baskets)):
                # If basket is big enough and hasn't been used yet (not 0)
                if baskets[i] >= fruit:
                    baskets[i] = 0  # Mark this basket as used up
                    matched = True
                    break

            if not matched:
                unplaced_count += 1

        return unplaced_count