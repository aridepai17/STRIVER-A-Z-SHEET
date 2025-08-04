# REARRANGE ARRAY BY SIGNS

'''
There is an array nums of size n with an equal number of positive and negative elements.
Without altering the relative order of positive and negative numbers, you must return an array of alternative positive and negative values.
Start the array with a positive number. 
'''

def rearrangeArray(nums):
    positives = [ num for num in nums if num >= 0]
    negatives = [ num for num in nums if num < 0 ]
    
    result = []
    i, j = 0, 0
    
    while i < len(positives) and j < len(negatives):
        result.append(positives[i])
        result.append(negatives[i])
        i  += 1
        j += 1 
        
    return result

# Examples 
nums1 = [1, 2, -4, -5]
print(rearrangeArray(nums1)) # Output: 1 -4  2 -5

# New examples
nums2 = [1, -1, 2, -2]
print(rearrangeArray(nums2)) # Output: 1 -1 2 -2

nums3 = [3, -3, 4, -4, 5, -5]
print(rearrangeArray(nums3)) # Output: 3 -3 4 -4 5 -5

nums4 = [10, -10, 20, -20]
print(rearrangeArray(nums4)) # Output: 10 -10 20 -20

nums5 = [5, -1, 6, -2, 7, -3]
print(rearrangeArray(nums5)) # Output: 5 -1 6 -2 7 -3

nums6 = [2, -2, 3, -3, 4, -4]
print(rearrangeArray(nums6)) # Output: 2 -2 3 -3 4 -4

nums7 = [8, -8, 9, -9]
print(rearrangeArray(nums7)) # Output: 8 -8 9 -9

nums8 = [6, -6, 1, -1]
print(rearrangeArray(nums8)) # Output: 6 -6 1 -1

nums9 = [4, -4, 5, -5, 6, -6]
print(rearrangeArray(nums9)) # Output: 4 -4 5 -5 6 -6

nums10 = [7, -7, 8, -8, 9, -9]
print(rearrangeArray(nums10)) # Output: 7 -7 8 -8 9 -9