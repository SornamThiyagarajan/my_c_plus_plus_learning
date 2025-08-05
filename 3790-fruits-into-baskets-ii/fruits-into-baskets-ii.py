class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        m = len(baskets)
        used = [False] * m  # Tracks if a basket is already used
        unplaced_count = 0

        for fruit in fruits:
            placed = False
            for i in range(m):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True  # Mark basket as used
                    placed = True
                    break
            if not placed:
                unplaced_count += 1

        return unplaced_count