# 4 SUM 

'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
1. 0 <= a, b, c, d < n
2. a, b, c, and d are distinct.
3. nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
'''

def fourSum(nums, target):
    result = []
    n = len(nums)
    nums.sort()
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue 
            
            left = j + 1
            right = n - 1
            
            while left < right:
                totalSum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if totalSum < target:
                    left += 1
                elif totalSum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
    return result

# Examples
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print(fourSum(nums1, target1)) # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Additional examples
nums2 = [2, 2, 2, 2]
target2 = 8
print(fourSum(nums2, target2)) # Output: [[2,2,2,2]]

nums3 = [1, 2, 3, 4, 5]
target3 = 10
print(fourSum(nums3, target3)) # Output: [[1,2,3,4]]

nums4 = [0, 0, 0, 0]
target4 = 0
print(fourSum(nums4, target4)) # Output: [[0,0,0,0]]

nums5 = [-1, 0, 1, 2, -1, -4]
target5 = -1
print(fourSum(nums5, target5)) # Output: [[-1,-1,0,2]]

nums6 = [1, 1, 1, 1, 1]
target6 = 4
print(fourSum(nums6, target6)) # Output: [[1,1,1,1]]

nums7 = [0, 1, 2, -1, -1, -2]
target7 = 0
print(fourSum(nums7, target7)) # Output: [[-2,-1,1,2],[-1,0,1,0]]

nums8 = [1, 2, 3, 4, 5, 6]
target8 = 18
print(fourSum(nums8, target8)) # Output: [[3,4,5,6]]

nums9 = [1, 2, 2, 2, 3, 4]
target9 = 9
print(fourSum(nums9, target9)) # Output: [[2,2,2,3]]

nums10 = [1, 2, 3, 4, 5, 6, 7, 8]
target10 = 30
print(fourSum(nums10, target10)) # Output: []