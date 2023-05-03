class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1=set(nums1)-set(nums2)
        diff2=set(nums2)-set(nums1)
        return [list(diff1),list(diff2)]