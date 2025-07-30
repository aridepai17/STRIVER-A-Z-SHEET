# COUNTING FREQUENCIES OF  ARRAY ELEMENTS 

'''
Given an array nums of size n which may contain duplicate elements, return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
You may return the result in any order, but each element must appear exactly once in the output.
'''

def countFrequencies(nums):
    n = len(nums)
    freq = {}
    
    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq [nums[i]] = 1
            
        result = []
        
        for key in freq:
            result.append((key, freq[key]))
            
        return result
    
# Examples 

# Example 1
nums1 = [1, 2, 2, 3, 3, 3]
print(f"Frequencies for {nums1}: {countFrequencies(nums1)}")
# Output: [(1, 1), (2, 2), (3, 3)]

# Example 2
nums2 = [4, 5, 6, 4, 5, 4]
print(f"Frequencies for {nums2}: {countFrequencies(nums2)}")
# Output: [(4, 3), (5, 2), (6, 1)]

# Example 3
nums3 = [7, 8, 9, 7, 8, 7, 9]
print(f"Frequencies for {nums3}: {countFrequencies(nums3)}")
# Output: [(7, 3), (8, 2), (9, 2)]

# Example 4
nums4 = [10, 10, 10, 10]
print(f"Frequencies for {nums4}: {countFrequencies(nums4)}")
# Output: [(10, 4)]

# Example 5
nums5 = []
print(f"Frequencies for {nums5}: {countFrequencies(nums5)}")
# Output: []

# Example 6
nums6 = [1, 1, 2, 3, 4, 4, 4]
print(f"Frequencies for {nums6}: {countFrequencies(nums6)}")
# Output: [(1, 2), (2, 1), (3, 1), (4, 3)]

# Example 7
nums7 = [5, 5, 5, 6, 7, 7, 8]
print(f"Frequencies for {nums7}: {countFrequencies(nums7)}")
# Output: [(5, 3), (6, 1), (7, 2), (8, 1)]

# Example 8
nums8 = [9, 10, 10, 11, 12, 12, 12]
print(f"Frequencies for {nums8}: {countFrequencies(nums8)}")
# Output: [(9, 1), (10, 2), (11, 1), (12, 3)]

# Example 9
nums9 = [13, 14, 15, 13, 14, 13]
print(f"Frequencies for {nums9}: {countFrequencies(nums9)}")
# Output: [(13, 3), (14, 2), (15, 1)]

# Example 10
nums10 = [16, 17, 18, 19, 20, 20, 20, 19]
print(f"Frequencies for {nums10}: {countFrequencies(nums10)}")
# Output: [(16, 1), (17, 1), (18, 1), (19, 2), (20, 3)] 