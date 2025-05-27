class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        start = 0
        max_len = 0

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = end
            max_len = max(max_len, end - start + 1)

        return max_len