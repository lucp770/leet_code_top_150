"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.




"""




class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        r_pointer = len(nums1)-1
        p1= m-1#the first non zero element of nums1
        p2 =n-1

        while r_pointer > -1 and p2 > -1:
            # iterate while in the rage of nums1
            if nums1[p1] > nums2[p2]:
                nums1[r_pointer] = nums1[p1]
                if p1 > 0:
                    p1-=1
                else:
                    nums1[0] = nums2[p2]
            else: 
                nums1[r_pointer] = nums2[p2]
                p2-=1

            r_pointer -=1


     
