class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Group characters and count consecutive length
        groups = []
        prev = None
        count = 0
        for c in word:
            if c == prev:
                count += 1
            else:
                if prev is not None:
                    groups.append((prev, count))
                prev = c
                count = 1
        groups.append((prev, count))

        # Collect lengths of groups > 1
        repeated_groups_lengths = [length for _, length in groups if length > 1]

        if not repeated_groups_lengths:
            # No group repeated, only 1 original string possible
            return 1

        total = sum(repeated_groups_lengths)  # sum of output lengths of repeated groups
        duplicates = len(repeated_groups_lengths) - 1

        return total - duplicates