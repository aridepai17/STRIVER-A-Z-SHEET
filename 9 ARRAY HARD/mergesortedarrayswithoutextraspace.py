# MERGE SORTED ARRAYS WITHOUT EXTRA SPACE 

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

def merge(nums1, m, nums2, n):
    last = m + n - 1 
    
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
        
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
        
# Examples 
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n)) # Output: [1, 2, 2, 3, 5, 6]

# Additional examples
nums3 = [1,2,3,0,0,0]
m = 3
nums4 = [0,0,0]
n = 3
print(merge(nums3, m, nums4, n)) # Output: [0, 0, 0, 1, 2, 3]

nums5 = [0,0,0,0,0,0]
m = 0
nums6 = [1,2,3]
n = 3
print(merge(nums5, m, nums6, n)) # Output: [1, 2, 3]

nums7 = [1,3,5,0,0,0]
m = 3
nums8 = [2,4,6]
n = 3
print(merge(nums7, m, nums8, n)) # Output: [1, 2, 3, 4, 5, 6]

nums9 = [1,2,3,0,0,0]
m = 3
nums10 = [4,5,6]
n = 3
print(merge(nums9, m, nums10, n)) # Output: [1, 2, 3, 4, 5, 6]

nums11 = [1,2,3,0,0,0]
m = 3
nums12 = [1,2,3]
n = 3
print(merge(nums11, m, nums12, n)) # Output: [1, 1, 2, 2, 3, 3]

nums13 = [0,0,0,0,0,0]
m = 0
nums14 = [1,2,3,4,5]
n = 5
print(merge(nums13, m, nums14, n)) # Output: [1, 2, 3, 4, 5]

nums15 = [1,1,1,0,0,0]
m = 3
nums16 = [1,1,1]
n = 3
print(merge(nums15, m, nums16, n)) # Output: [1, 1, 1, 1, 1, 1]

nums17 = [2,0,0,0,0,0]
m = 1
nums18 = [1,2,3,4,5]
n = 5
print(merge(nums17, m, nums18, n)) # Output: [1, 2, 2, 3, 4, 5]

nums19 = [0,0,0,0,0,0]
m = 0
nums20 = [0,0,0,0,0]
n = 5
print(merge(nums19, m, nums20, n)) # Output: [0, 0, 0, 0, 0, 0]