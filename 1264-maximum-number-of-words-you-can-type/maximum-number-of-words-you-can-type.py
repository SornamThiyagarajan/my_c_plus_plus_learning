class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Put broken letters into a set for quick lookup
        broken = set(brokenLetters)
        
        # Split text into words
        words = text.split()
        
        count = 0
        for word in words:
            # If no broken letter is in the word, it's valid
            if not (set(word) & broken):  # intersection check
                count += 1
        return count