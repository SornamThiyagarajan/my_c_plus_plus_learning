class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0 
        output = []
        for num in nums:
            current_sum += num
            output.append(current_sum)
        return output