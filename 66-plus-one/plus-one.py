class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        for i in range(n - 1, -1, -1):
            # If the digit is less than 9, just add one and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set current digit to 0 and continue
            digits[i] = 0
        
        # If we exited the loop, all digits were 9 (e.g., 999 → 1000)
        return [1] + [0] * n