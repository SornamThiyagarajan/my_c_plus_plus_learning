class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
           return []
    
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            # If current number is not consecutive
            if nums[i] != nums[i-1] + 1:
                # Add the previous range
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i-1]}")
                start = nums[i]  # start a new range
        
        # Add the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{nums[-1]}")
        
        return ranges