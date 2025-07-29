class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Set current to 0 and carry will continue

        # If all were 9s, then we need to add 1 at the front
        return [1] + digits
