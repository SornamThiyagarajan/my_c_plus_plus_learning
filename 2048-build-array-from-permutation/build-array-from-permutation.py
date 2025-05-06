class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        inp_idx = [(x,nums[x]) for x in range(len(nums))]      
        for i in range(0,len(nums)):               
            idx_temp = nums[i]
            ans.append(inp_idx[idx_temp][1])           
        return ans
        