class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_m = len(nums1)
        while(m>=1 and n>=1):
            if nums1[m-1]>=nums2[n-1]:
                nums1[len_m-1] = nums1[m-1]
                m -=1   
            else:
                nums1[len_m-1] = nums2[n-1]
                n -=1
            len_m -=1          


        if n==0:
            return 
        else:
            for i in range(0,n):
                nums1[i] = nums2[i]     
        