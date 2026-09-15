class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        l=len(res)
        r1=float(res[l//2])
        r2=(res[l//2]+res[(l//2)-1])/2.0
        if l%2==0:
            return r2
        else:
            return r1