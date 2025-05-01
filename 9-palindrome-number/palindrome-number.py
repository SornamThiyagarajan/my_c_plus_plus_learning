class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_num = str(x)
        return input_num == input_num[::-1]
