class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple
        
        # Apply sign
        result = -result if negative else result
        
        # Clamp to 32-bit range
        return max(INT_MIN, min(INT_MAX, result))