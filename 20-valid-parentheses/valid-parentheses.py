class Solution:
    def isValid(self, s: str) -> bool:

        
        stack = []  # Create a empty stack for push and pop 
        bracket_dict =  {'{':'}', '(':')', '[':']'} # Create a dictionary bracket for all braces 


        # Iterate through given expression and push to stack if open braces 
        for each in s : 
            if each in [ '{', '(', '['] :
                 stack.append(each)
            else:  # If no open braces and contains closing braces perform stack pop 
                if stack: 
                    top = stack.pop()
                    if bracket_dict[top] != each: 
                        return False
                else: 
                    return False
        return False if stack else True   #if stack is empty and open and close braces counts are matching then return TRUE
        