# MAJORITY ELEMENT 1

'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

def majorityElement(nums):
    candidate = 0
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
        
    return candidate 

# Examples 
nums1 = [3, 2, 3]
print(majorityElement(nums1)) # Output: 3 

# Additional examples
nums2 = [2, 2, 1, 1, 1, 2, 2]  # Output: 2
print(majorityElement(nums2)) # Output: 2

nums3 = [1, 1, 1, 2, 2, 2, 1]  # Output: 1
print(majorityElement(nums3)) # Output: 1

nums4 = [5, 5, 5, 1, 1, 2, 5]  # Output: 5
print(majorityElement(nums4)) # Output: 5

nums5 = [1]  # Output: 1
print(majorityElement(nums5)) # Output: 1

nums6 = [2, 2, 2, 3, 3]  # Output: 2
print(majorityElement(nums6)) # Output: 2

nums7 = [4, 4, 4, 4, 5, 5, 5]  # Output: 4
print(majorityElement(nums7)) # Output: 4

nums8 = [6, 6, 6, 7, 7, 7, 6]  # Output: 6
print(majorityElement(nums8)) # Output: 6

nums9 = [8, 8, 8, 8, 9, 9]  # Output: 8
print(majorityElement(nums9)) # Output: 8

nums10 = [10, 10, 10, 10, 10, 1, 1]  # Output: 10
print(majorityElement(nums10)) # Output: 10 