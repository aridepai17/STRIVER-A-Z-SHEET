# MEDIAN OF TWO SORTED ARRAYS

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

def findMedianSortedArrays(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    
    if n1 > n2:
        return findMedianSortedArrays(nums2, nums1)
    
    n = n1 + n2
    
    left = (n1 + n2 + 1) // 2
    
    low = 0
    high = n1
    
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
            
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]
            
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
            
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
            
# Examples
nums1 = [1,3], nums2 = [2]
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.0

nums3 = [1,2], nums4 = [3,4]
print(findMedianSortedArrays(nums3, nums4)) # Output: 2.5

nums5 = [0,0], nums6 = [0,0]
print(findMedianSortedArrays(nums5, nums6)) # Output: 0.0

nums7 = [], nums8 = [1]
print(findMedianSortedArrays(nums7, nums8)) # Output: 1.0

nums9 = [2], nums10 = []
print(findMedianSortedArrays(nums9, nums10)) # Output: 2.0

nums11 = [1,3,5,7,9], nums12 = [2,4,6,8,10]
print(findMedianSortedArrays(nums11, nums12)) # Output: 5.5

nums13 = [1,2,3,4,5], nums14 = [6,7,8,9,10]
print(findMedianSortedArrays(nums13, nums14)) # Output: 5.5

nums15 = [1,1,1,1,1], nums16 = [2,2,2,2,2]
print(findMedianSortedArrays(nums15, nums16)) # Output: 1.5

nums17 = [1,2,3], nums18 = [4,5,6,7,8,9]
print(findMedianSortedArrays(nums17, nums18)) # Output: 5.0

nums19 = [1,2,3,4,5,6,7,8,9,10], nums20 = [11,12,13,14,15]
print(findMedianSortedArrays(nums19, nums20)) # Output: 7.0