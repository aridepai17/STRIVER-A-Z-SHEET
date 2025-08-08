# 3 SUM 

'''
Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. 
One element can be a part of multiple triplets. The output and the triplets can be returned in any order.
'''

def threeSum(nums):
    n = len(nums)
    result = []
    nums.sort()
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        
        while left < right:
            totalSum = nums[i] + nums[left] + nums[right]
            if totalSum < 0:
                left += 1
            elif totalSum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
    return result
        
# Example 
nums1 = [2, -2, 0, 3, -3, 5]
print(threeSum(nums1)) # Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]

# Additional examples
# Example 1
nums2 = [0, 0, 0, 0]
print(threeSum(nums2)) # Output: [[0, 0, 0]]

# Example 2
nums3 = [-1, 0, 1]
print(threeSum(nums3)) # Output: [[-1, 0, 1]]

# Example 3
nums4 = [-1, 1, 0, 2, -2]
print(threeSum(nums4)) # Output: [[-2, 0, 2], [-1, 1, 0]]

# Example 4
nums5 = [1, 2, -2, -1]
print(threeSum(nums5)) # Output: [[-2, -1, 1]]

# Example 5
nums6 = [3, 0, -3, 1, 1]
print(threeSum(nums6)) # Output: [[-3, 0, 3]]

# Example 6
nums7 = [1, 2, -2, -1, -1, 0]
print(threeSum(nums7)) # Output: [[-2, -1, 1]]

# Example 7
nums8 = [0, 0, 0, 0, 0]
print(threeSum(nums8)) # Output: [[0, 0, 0]]

# Example 8
nums9 = [-4, -2, 1, 2, 3]
print(threeSum(nums9)) # Output: [[-4, 1, 3], [-2, -2, 4]]

# Example 9
nums10 = [1, 1, -2, -2, 0]
print(threeSum(nums10)) # Output: [[-2, 1, 1]]

# Example 10
nums11 = [0, 1, 2, -1, -1, -2]
print(threeSum(nums11)) # Output: [[-2, 1, 1], [-1, 0, 1]]