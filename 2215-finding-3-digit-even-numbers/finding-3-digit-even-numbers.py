class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        op_arr = []
        for i in range(len(digits)): ##digit_1 for loop 
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if (i!=j) and (j!=k) and (i!=k):  ##to confirm not all numbers are same (unique)
                        num = digits[i]*100 + digits[j]*10 + digits[k]
                        if (num%2==0) and ((len(str(num))) == 3):
                            op_arr.append(num)

        return sorted(set(op_arr))
