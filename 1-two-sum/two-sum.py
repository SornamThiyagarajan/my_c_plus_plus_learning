class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, num in enumerate(nums):            
            complement = target - num 
            if complement in nums_map : 
                return [nums_map[complement],idx]
            
            nums_map[num] = idx 