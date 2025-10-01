class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_bottles = empty // numExchange
            drunk += new_bottles
            empty = empty % numExchange + new_bottles
        
        return drunk #