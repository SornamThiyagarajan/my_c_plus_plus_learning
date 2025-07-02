class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        max_right = [0] * n
        max_right[-1] = nums[-1]
        
        # Fill max_right: max element to the right of index i
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])
        
        result = float('-inf')
        max_left = nums[0]
        
        for j in range(1, n - 1):
            max_left = max(max_left, nums[j - 1])
            value = (max_left - nums[j]) * max_right[j + 1]
            result = max(result, value)
        
        return max(result, 0) ###