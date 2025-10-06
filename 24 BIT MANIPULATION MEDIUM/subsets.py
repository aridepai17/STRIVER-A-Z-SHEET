# SUBSETS

'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def subsets(nums):
    n = len(nums)
    subsets = 1 << n
    powerSet = []
    
    for num in range(subsets):
        currentSubset = []
        for i in range(n):
            if num & 1 << i:
                currentSubset.append(nums[i])
        
        powerSet.append(currentSubset)
        
    return powerSet

'''
Time Complexity: O(n * 2^n)
Let n be the number of elements in the input array `nums`.
The total number of possible subsets is 2^n.
The outer loop iterates 2^n times, once for each possible subset represented by a number from 0 to 2^n - 1.
Inside the outer loop, the inner loop runs n times to check each bit of the number. This determines which elements from the original `nums` array to include in the current subset.
Thus, for each of the 2^n subsets, we perform n operations, leading to a time complexity of O(n * 2^n).

Space Complexity: O(n * 2^n)
The space complexity is determined by the space required to store the output, `powerSet`.
There are 2^n subsets in total. The total number of elements across all these subsets is n * 2^(n-1).
For example, if nums has 3 elements, there are 2^3 = 8 subsets. The total number of elements in the power set is 3 * 2^(3-1) = 12.
Therefore, the space required to store the result is proportional to n * 2^n.
'''

# Test Cases
nums1 = [1, 2, 3]
print(subsets(nums1)) # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

nums2 = []
print(subsets(nums2)) # Output: [[]]

nums3 = [0]
print(subsets(nums3)) # Output: [[], [0]]

nums4 = [4, 5]
print(subsets(nums4)) # Output: [[], [4], [5], [4, 5]]

nums5 = [1, 2, 3, 4]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
print(subsets(nums5))

nums6 = [10, 20]
print(subsets(nums6)) # Output: [[], [10], [20], [10, 20]]

nums7 = [-1, -2]
print(subsets(nums7)) # Output: [[], [-1], [-2], [-1, -2]]

nums8 = [-1, 0, 1]
print(subsets(nums8)) # Output: [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]

nums9 = [100]
print(subsets(nums9)) # Output: [[], [100]]

nums10 = [7, 8, 9]
print(subsets(nums10)) # Output: [[], [7], [8], [7, 8], [9], [7, 9], [8, 9], [7, 8, 9]]