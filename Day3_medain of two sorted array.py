class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # we first merge both array  into one and sort after merging 
        for i in nums2:
            nums1.append(i)
            nums1.sort()

        #here we find the length of array after merging
        n=len(nums1)

        #now apply median fromula for id length of array is even 
        if n%2==0:
            median=(nums1[n//2-1]+nums1[n//2])/2.0
        #here we apply if length of array is odd
        else:
            median=(nums1[n//2])

        return median

nums1=[1,2]
nums2=[3]

res=Solution()
print(f"The median of two sorted array if {res.findMedianSortedArrays(nums1, nums2)}")


        
