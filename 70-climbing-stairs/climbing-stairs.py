class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
           return n
        a, b = 1, 2  # ways(1), ways(2)
        for _ in range(3, n + 1):
            a, b = b, a + b  # shift window
        return b