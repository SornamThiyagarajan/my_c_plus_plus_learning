class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: 
            return 0
        
        binary = ""
        set_bit_count = 0 
        while n > 0:
            remainder = n % 2 
            binary = str(remainder) + binary 
            if remainder == 1: 
                set_bit_count += 1 
            n = n//2 

        return set_bit_count 
        
