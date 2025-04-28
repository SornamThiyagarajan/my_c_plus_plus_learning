class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        sum_ = 0
        count = 0
        
        for right in range(n):
            sum_ += nums[right]
            
            while left <= right and sum_ * (right - left + 1) >= k:
                sum_ -= nums[left]
                left += 1
                
            count += right - left + 1
        
        return count