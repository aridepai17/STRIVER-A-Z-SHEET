# SINGLE ELEMENT IN SORTED ARRAY


'''
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
'''

def singleNonDuplicate(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid 
    
    return nums[left]


# Examples 
nums1 = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums1)) # Output: 2

nums2 = [1,1,2,2,3,3,4,4,5]
print(singleNonDuplicate(nums2)) # Output: 5

nums3 = [0,1,1,2,2,3,3,4,4]
print(singleNonDuplicate(nums3)) # Output: 0

nums4 = [1,1,2,2,3,4,4,5,5]
print(singleNonDuplicate(nums4)) # Output: 3

nums5 = [10,10,11,11,12,13,13,14,14,15,15]
print(singleNonDuplicate(nums5)) # Output: 12

nums6 = [-5,-5,-3,-3,-2,-1,-1,0,0]
print(singleNonDuplicate(nums6)) # Output: -2

nums7 = [2,2,3,3,4,4,5,6,6]
print(singleNonDuplicate(nums7)) # Output: 5

nums8 = [7]
print(singleNonDuplicate(nums8)) # Output: 7

nums9 = [100,100,101,101,102,102,103,104,104]
print(singleNonDuplicate(nums9)) # Output: 103

nums10 = [-4,-4,-2,-2,-1,0,0,1,1]
print(singleNonDuplicate(nums10)) # Output: -1