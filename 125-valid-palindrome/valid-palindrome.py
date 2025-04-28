import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = s.lower()      
        result = ''.join(c.lower() for c in s if c.isalnum())
        if result == result[::-1]:
            return True 
        else:
            return False

  