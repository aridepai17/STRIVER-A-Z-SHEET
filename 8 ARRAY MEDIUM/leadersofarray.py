# LEADERS IN AN ARRAY 

'''
Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. 
The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.
'''

def leaders(nums):
    n = len(nums)
    maxsofar = nums[-1]
    result = []
    result.append(maxsofar)
    
    for i in range(n - 2, -1, -1):
        if nums[i] > maxsofar:
            maxsofar = nums[i]
            result.append(maxsofar)
            
    result.reverse()
    return result 

# Examples 
nums1 = [1, 2, 5, 3, 1, 2]
print(leaders(nums1)) # Output: [5, 3, 2]

# New examples
nums2 = [16, 17, 4, 3, 5, 2]
print(leaders(nums2)) # Output: [17, 5, 2]

nums3 = [1, 2, 3, 4, 5]
print(leaders(nums3)) # Output: [5]

nums4 = [5, 4, 3, 2, 1]
print(leaders(nums4)) # Output: [5]

nums5 = [10, 20, 30, 40, 50]
print(leaders(nums5)) # Output: [50]

nums6 = [5, 10, 5, 2, 1]
print(leaders(nums6)) # Output: [10, 5, 2, 1]

nums7 = [3, 2, 1, 4, 5]
print(leaders(nums7)) # Output: [5]

nums8 = [1, 3, 2, 5, 4]
print(leaders(nums8)) # Output: [5, 4]

nums9 = [7, 5, 6, 4, 3]
print(leaders(nums9)) # Output: [7, 6, 4, 3]

nums10 = [1, 2, 3, 2, 1, 0]
print(leaders(nums10)) # Output: [3, 2, 1, 0]