class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
    :type nums: List[int]
    :rtype: bool
    """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False