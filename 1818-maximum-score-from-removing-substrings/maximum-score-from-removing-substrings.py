class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, a, b, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score
        
        # Choose order based on which operation gives more points
        if x > y:
            s, score1 = remove_substring(s, 'a', 'b', x)
            s, score2 = remove_substring(s, 'b', 'a', y)
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)
            s, score2 = remove_substring(s, 'a', 'b', x)

        return score1 + score2