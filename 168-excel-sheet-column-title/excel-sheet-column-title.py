class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1  # adjust for 1-index
            remainder = columnNumber % 26
            res.append(chr(ord('A') + remainder))
            columnNumber //= 26
        return ''.join(reversed(res))
        ##