class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        max_end = 0
        for num in nums: 
            max_end += num
            max_so_far = max(max_so_far,max_end)
            if max_end < 0 : 
                max_end = 0 
        return max_so_far

        