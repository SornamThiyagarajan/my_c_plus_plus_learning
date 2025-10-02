class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        full = numBottles
        empty = 0
        current_exchange = numExchange
        
        while full > 0:
            # Drink all full bottles
            total_drunk += full
            empty += full
            full = 0
            
            # Exchange if possible
            if empty >= current_exchange:
                full += 1
                empty -= current_exchange
                current_exchange += 1
            else:
                break
        
        return total_drunk