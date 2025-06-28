class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
      # Pair each number with its index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value descending
        indexed_nums.sort(reverse=True, key=lambda x: x[0])
        
        # Pick top-k values with indices
        top_k = indexed_nums[:k]
        
        # Sort these by their original index to maintain order
        top_k.sort(key=lambda x: x[1])
        
        # Extract just the values
        return [num for num, _ in top_k]  