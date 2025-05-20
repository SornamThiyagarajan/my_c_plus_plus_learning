class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        count = [0] * (n + 1)  # Difference array for range counting

        # Mark range increments using a difference array
        for l, r in queries:
            count[l] += 1
            if r + 1 < len(count):
                count[r + 1] -= 1

        # Build the prefix sum to get the final coverage count per index
        for i in range(1, n):
            count[i] += count[i - 1]

        # Now check if every nums[i] <= count[i]
        for i in range(n):
            if nums[i] > count[i]:
                return False

        return True