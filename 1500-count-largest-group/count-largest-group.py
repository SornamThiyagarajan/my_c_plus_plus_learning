def find_digit(each):   
        sum_digit = 0
        while each:
            sum_digit += each % 10
            each//=10
        return sum_digit

class Solution(object):
    def countLargestGroup(self, n):
        groups = {} ##Creating dictionary 
        for each in range(1,n+1):        
            sum_dig = find_digit(each)
            if sum_dig not in groups:
                groups[sum_dig] =[]
            groups[sum_dig].append(each)       
        group_sizes = [len(group) for group in groups.values()]
        print(group_sizes)
        if group_sizes:
            max_size = max(group_sizes)
        else:
            max_size = 0

        count = group_sizes.count(max_size)
        #print(count)
        return count 
        