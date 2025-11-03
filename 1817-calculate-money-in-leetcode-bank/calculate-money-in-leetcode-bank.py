class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        
        # Full weeks sum
        week_sum = (28 * weeks) + (7 * weeks * (weeks - 1)) // 2
        
        # Remaining days sum
        extra = (days * (2 * (weeks + 1) + (days - 1))) // 2
        
        return week_sum + extra #sornam.t 