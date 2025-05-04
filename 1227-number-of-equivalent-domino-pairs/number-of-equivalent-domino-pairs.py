class Solution:
    from collections import defaultdict
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        res = 0
        
        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # Normalize the domino (e.g., [2,1] -> (1,2))
            res += count[key]           # Add the current number of similar dominoes seen so far
            count[key] += 1             # Increment the count of this normalized domino
            
        return res  ###