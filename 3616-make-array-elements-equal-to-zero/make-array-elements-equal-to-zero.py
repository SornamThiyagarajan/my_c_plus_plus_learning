class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        # simulate starting at `start` with direction `dir` (1 = right, -1 = left)
        def simulate(start, dir):
            arr = nums[:]  # copy
            curr = start
            direction = dir

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += direction
                else:
                    arr[curr] -= 1
                    direction *= -1  # reverse direction
                    curr += direction

            return all(x == 0 for x in arr)

        ans = 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, -1):
                    ans += 1
                if simulate(i, 1):
                    ans += 1

        return ans