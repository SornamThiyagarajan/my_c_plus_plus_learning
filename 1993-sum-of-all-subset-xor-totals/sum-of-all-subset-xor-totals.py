class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor
            # Choice 1: include nums[index]
            include = dfs(index + 1, current_xor ^ nums[index])
            # Choice 2: exclude nums[index]
            exclude = dfs(index + 1, current_xor)
            return include + exclude
        
        return dfs(0, 0)