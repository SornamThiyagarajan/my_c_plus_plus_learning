class Solution:
    def addBinary(self, a: str, b: str) -> str:
            result = []
            carry = 0
            
            # Start from the end of both strings
            i, j = len(a) - 1, len(b) - 1
            
            while i >= 0 or j >= 0 or carry:
                # Get the digit from a and b or 0 if index out of range
                digit_a = int(a[i]) if i >= 0 else 0
                digit_b = int(b[j]) if j >= 0 else 0
                
                # Sum of digits + carry
                total = digit_a + digit_b + carry
                carry = total // 2
                result.append(str(total % 2))
                
                i -= 1
                j -= 1
            
            # Reverse the result list and join to get the binary string
            return ''.join(reversed(result))