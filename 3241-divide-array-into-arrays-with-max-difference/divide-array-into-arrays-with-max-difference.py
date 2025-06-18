class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
            nums.sort()
            n = len(nums)
            res = []

            i = 0
            while i < n:
                # Try to form a group of 3 from current i
                if i + 2 < n and nums[i + 2] - nums[i] <= k:
                    res.append([nums[i], nums[i + 1], nums[i + 2]])
                    i += 3
                else:
                    return []  # Impossible to group satisfying the condition

            return res