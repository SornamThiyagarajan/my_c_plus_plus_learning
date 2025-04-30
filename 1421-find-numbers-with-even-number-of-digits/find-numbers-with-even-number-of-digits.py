class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0 
        for each in range(n):
            dig_len = len(str(nums[each]))
            if dig_len%2 == 0: 
                cnt += 1 
        return cnt