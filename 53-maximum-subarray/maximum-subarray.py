class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = nums[0]
        for num in range(len(nums)):
            temp = curr_sum+nums[num]
            if temp < nums[num]:
                curr_sum = nums[num]
            else:
                curr_sum = temp 

        
            
            if max_sum < curr_sum:
                max_sum = curr_sum 

        
        return max_sum