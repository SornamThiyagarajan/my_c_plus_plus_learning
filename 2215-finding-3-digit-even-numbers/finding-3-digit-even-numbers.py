class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        '''op_arr = []
        for i in range(len(digits)): ##digit_1 for loop 
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if (i!=j) and (j!=k) and (i!=k):  ##to confirm not all numbers are same (unique)
                        num = digits[i]*100 + digits[j]*10 + digits[k]
                        if (num%2==0) and ((len(str(num))) == 3):
                            op_arr.append(num)

        return sorted(set(op_arr))'''
        even_numbers = set()  # Use set to automatically avoid duplicates
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        a, b, c = digits[i], digits[j], digits[k]
                        
                        if a == 0:  # Leading zero not allowed in 3-digit numbers
                            continue
                        
                        if c % 2 != 0:  # Only consider even digits at unit place
                            continue

                        num = a * 100 + b * 10 + c
                        even_numbers.add(num)

        return sorted(even_numbers)
