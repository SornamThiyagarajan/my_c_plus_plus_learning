class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for each in range(len(arr)-2):
            if (arr[each] % 2 ) == 1 and (arr[each+1] % 2 )== 1 and (arr[each+2] % 2)== 1:
                return True 
        return False 

