class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count the frequency of each element
        freq = Counter(nums)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Sum the frequencies of elements that have the maximum frequency
        total = sum(count for count in freq.values() if count == max_freq)
        
        return total
