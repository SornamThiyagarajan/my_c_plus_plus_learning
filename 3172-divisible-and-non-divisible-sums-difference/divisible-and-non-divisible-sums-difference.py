class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        k = n // m
        div_sum = m * k * (k + 1) // 2
        non_div_sum = total_sum - div_sum
        return non_div_sum - div_sum
        ##