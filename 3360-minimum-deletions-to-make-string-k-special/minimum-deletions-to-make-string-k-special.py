class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        
        min_deletions = float('inf')
        
        for target in range(1, max(freq) + 1):
            deletions = 0
            for f in freq:
                if f < target:
                    deletions += f  # delete entire char group
                elif f > target + k:
                    deletions += f - (target + k)  # trim down
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions