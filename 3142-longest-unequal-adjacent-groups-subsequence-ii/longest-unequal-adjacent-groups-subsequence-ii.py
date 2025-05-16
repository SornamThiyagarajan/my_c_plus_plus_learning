class Solution:
    from typing import List
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming_distance(a: str, b: str) -> int:
            return sum(x != y for x, y in zip(a, b))
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        # Dynamic programming to find the longest valid subsequence
        for i in range(n):
            for j in range(i):
                if (groups[i] != groups[j] and
                    len(words[i]) == len(words[j]) and
                    hamming_distance(words[i], words[j]) == 1):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # Find the index of the last element in the longest subsequence
        max_index = max(range(n), key=lambda i: dp[i])

        # Reconstruct the subsequence
        result = []
        while max_index != -1:
            result.append(words[max_index])
            max_index = prev[max_index]

        return result[::-1]  # Reverse to get correct order

        