class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Last index for merged array
        i = m - 1  # last element in nums1
        j = n - 1  # last element in nums2
        k = m + n - 1  # last position in nums1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are leftover elements in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
