from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:       
        n = len(nums)
        # 1. Compute total distinct count
        distinct_total = len(set(nums))
        
        freq = Counter()
        have = 0
        ans = 0
        
        l = 0
        # 2. Slide r from 0 to n-1
        for r in range(n):
            # Add nums[r]
            freq[nums[r]] += 1
            if freq[nums[r]] == 1:
                have += 1
            
            # 3. While window [l..r] is complete, count and shrink from left
            while have == distinct_total:
                # All subarrays from l to any end ≥ r are complete
                ans += (n - r)
                
                # Remove nums[l] and advance l
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    have -= 1
                l += 1
        
        return ans
