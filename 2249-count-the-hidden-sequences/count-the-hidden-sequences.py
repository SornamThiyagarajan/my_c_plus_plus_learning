class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(differences)
        # Compute the prefix sums of differences
        prefix_sum = [0] * (n + 1)  # prefix_sum[i] represents the cumulative sum of differences up to index i
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + differences[i]
        
        # The range for hidden[0] must satisfy:
        min_x0 = lower - min(prefix_sum)  # Lower bound for x0
        max_x0 = upper - max(prefix_sum)  # Upper bound for x0
        
        # Count the number of valid x0 values in the range [min_x0, max_x0]
        return max(0, max_x0 - min_x0 + 1)