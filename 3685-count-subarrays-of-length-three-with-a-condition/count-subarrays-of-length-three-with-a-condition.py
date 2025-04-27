class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0 
        output_arr = []
        for each in range(1, len(nums)-1):
            
            curr = nums[each]
            prev = nums[each-1]
            nxt = nums[each+1]
            if (prev+nxt) == (curr/2):            
                count = count+1
                output_arr.append(prev)
                output_arr.append(curr)
                output_arr.append(nxt)
        
        if len(output_arr)==0:
            return 0 
        else:
            return count 
