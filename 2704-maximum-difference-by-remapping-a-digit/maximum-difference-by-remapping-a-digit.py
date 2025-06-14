class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
    
        # Find max number
        max_num = num_str
        for d in num_str:
            if d != '9':
                # Replace all occurrences of d with '9'
                max_num = num_str.replace(d, '9')
                break
        
        # Find min number
        min_num = num_str
        first_digit = num_str[0]
        
        # Try replacing first digit with '0' if it's not '0'
        if first_digit != '0':
            min_num = num_str.replace(first_digit, '0')
        else:
            # If first digit is '0', find first digit from left that's not '0' or '1' (since replacing with '0' might be better)
            for d in num_str:
                if d != '0' and d != '1':
                    min_num = num_str.replace(d, '0')
                    break
        
        return int(max_num) - int(min_num)