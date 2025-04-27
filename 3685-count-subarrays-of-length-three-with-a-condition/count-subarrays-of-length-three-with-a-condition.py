class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0 
        output_arr = []
        for each in range(1, len(nums)-1):
            #print(nums[each])
            curr = nums[each]
            prev = nums[each-1]
            nxt = nums[each+1]
            #print("\nCurrent Element:",nums[each])
            #print("Prev Element:",nums[each-1])
            #print("Next Element:",nums[each+1])           
            #print("Sum:",prev+nxt)
            #print("Condn:",curr/2)
            #print("***")
            if (prev+nxt) == (curr/2):
                #print("Pass")
                count = count+1
                output_arr.append(prev)
                output_arr.append(curr)
                output_arr.append(nxt)
        
        if len(output_arr)==0:
            return 0 
        else:
            return count 
