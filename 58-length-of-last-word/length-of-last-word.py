class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split() 
        last_word = words[-1]
        length = len(last_word)
        return length 