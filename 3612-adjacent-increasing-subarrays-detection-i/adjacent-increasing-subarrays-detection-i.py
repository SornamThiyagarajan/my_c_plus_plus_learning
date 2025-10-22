class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        if n < 2 * k:
            return False

        # inc[i] = length of strictly increasing streak ending at i
        inc = 1
        streak = [0] * n
        streak[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                inc = 1
            streak[i] = inc

        # Check pairs of adjacent subarrays
        for a in range(n - 2 * k + 1):
            if streak[a + k - 1] >= k and streak[a + 2 * k - 1] >= k:
                return True

        return False
