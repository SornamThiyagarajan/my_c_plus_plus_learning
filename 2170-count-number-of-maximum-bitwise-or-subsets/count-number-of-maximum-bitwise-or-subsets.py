class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        count = 0
        
        def dfs(i, curr_or):
            nonlocal count
            if i == len(nums):
                if curr_or == max_or:
                    count += 1
                return
            # Include nums[i]
            dfs(i + 1, curr_or | nums[i])
            # Exclude nums[i]
            dfs(i + 1, curr_or)
        
        dfs(0, 0)
        return count