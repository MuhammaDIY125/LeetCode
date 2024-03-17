class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        lst = sorted(nums1 + nums2)
        n = len(lst)
        if n % 2:
            return lst[(n // 2)]
        return (lst[(n // 2)] + lst[(n // 2)-1]) / 2

nums1 = [1, 3]
nums2 = [2, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))