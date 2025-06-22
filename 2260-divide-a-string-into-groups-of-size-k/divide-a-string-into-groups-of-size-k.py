class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        n = len(s)
        
        for i in range(0, n, k):
            # Extract group of size k (may be shorter for last group)
            group = s[i:i+k]
            # If last group is smaller than k, fill it with the fill character
            if len(group) < k:
                group += fill * (k - len(group))
            result.append(group)
        
        return result