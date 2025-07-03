class Solution:
    def kthCharacter(self, k: int) -> str:
        def next_char(c):
            return 'a' if c == 'z' else chr(ord(c) + 1)

        def helper(k, ch, depth):
            if depth == 0:
                return ch
            half = 1 << (depth - 1)  # length of one half
            if k <= half:
                return helper(k, ch, depth - 1)
            else:
                return helper(k - half, next_char(ch), depth - 1)

        # Find minimum depth such that 2^depth >= k
        depth = 0
        while (1 << depth) < k:
            depth += 1

        return helper(k, 'a', depth)