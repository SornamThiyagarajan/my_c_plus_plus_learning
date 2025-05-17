class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] >= nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp 
        print(nums)
        