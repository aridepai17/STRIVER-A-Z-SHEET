# SINGLE NUMBER

'''
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

def singleNumber(nums):
    xor = 0
    
    for num in nums:
        xor ^= num
        
    return xor

'''
Time Complexity: O(n)
We iterate through the nums array once. The XOR operation is a constant time operation.
Therefore, the time complexity is linear with respect to the number of elements in the input array.

Space Complexity: O(1)
We only use a single integer variable 'xor' to store the result.
The space required does not grow with the size of the input array, so it is constant.
'''

# Test Cases
nums1 = [2,2,1]
print(singleNumber(nums1)) # Output: 1

nums2 = [4,1,2,1,2]
print(singleNumber(nums2)) # Output: 4

nums3 = [1]
print(singleNumber(nums3)) # Output: 1

nums4 = [1, 0, 1]
print(singleNumber(nums4)) # Output: 0

nums5 = [-1, -1, -2]
print(singleNumber(nums5)) # Output: -2

nums6 = [9, 9, 8, 8, 7, 7, 5]
print(singleNumber(nums6)) # Output: 5

nums7 = [100, 200, 100, 200, 300]
print(singleNumber(nums7)) # Output: 300

nums8 = [0, 0, 5, 5, -10]
print(singleNumber(nums8)) # Output: -10

nums9 = [1, 2, 3, 4, 5, 1, 2, 3, 4]
print(singleNumber(nums9)) # Output: 5

nums10 = [17, 12, 5, -6, 12, 4, 17, -6, 5]
print(singleNumber(nums10)) # Output: 4