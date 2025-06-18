class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        odd_freqs = [v for v in freq.values() if v % 2 == 1]
        even_freqs = [v for v in freq.values() if v % 2 == 0]

        if not odd_freqs or not even_freqs:
            return -1

        max_diff = max(o - e for o in odd_freqs for e in even_freqs)
        return max_diff