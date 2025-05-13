class Solution:
    
    def lengthAfterTransformations(self, s: str, t: int) -> int:   
            MOD = 10**9 + 7
            dp = [[0] * (t + 1) for _ in range(26)]

            # Base case: length of any character after 0 transformations is 1
            for ch in range(26):
                dp[ch][0] = 1

            # Fill DP table
            for i in range(1, t + 1):
                for ch in range(26):
                    if ch == 25:  # 'z'
                        # 'z' → 'ab' → becomes 'a' and 'b'
                        dp[ch][i] = (dp[0][i - 1] + dp[1][i - 1]) % MOD
                    else:
                        # Other chars → go to next char
                        dp[ch][i] = dp[ch + 1][i - 1]

            # Count frequency of each character in input
            count = Counter(s)
            total = 0

            for ch, freq in count.items():
                idx = ord(ch) - ord('a')
                total = (total + freq * dp[idx][t]) % MOD

            return total