class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0
        for word in text.split():
            if not any(ch in broken for ch in word):
                count += 1
        return count