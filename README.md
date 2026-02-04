# Median-of-two-sorted-array
We find the median of two sorted array by first merge the two array into one then sorted in ascending order and then apply the condition of if-else and apply the median formula for even and odd then apply on conditon and return the median 

# Apporach
===============
1.first merge or append  second array into first by iterating the element of second array into first
2. sort the array 1 into after merging 
3. then find the length of array 
4. apply the if -esle conditon on it to find the median 
5. if the length of array is even the apply the even fromula of median median = nums(n//2-1)+nums(n//2)/2
6. if the length is odd then apply median = nums(n//2)
7. then return the median of array as output 

# Time complexity O(log(m+n))

# Space complexity is O(1) because without using extra space

# Dry run 

Example nums1=[1,2]
nums2=[3]

after merging nums1=[1,2,3]
length of array n=3
#we apply this feomula is length is even but here if condition is false it goes to esle condtion 
 if  n%2==0:
 then median =(nums1[n//2-1]+nums1[n//2)/2

 so on else conditon
 else:
 median=(nums1[3//2)
 so the medain is 2nd elementnafter divide

 then we return  2 as a median 
 
 

