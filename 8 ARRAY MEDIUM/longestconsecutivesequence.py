# LONGEST CONSECUTIVE SEQUENCE 

'''
iven an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

def longestConsecutive(nums):
    numSet = set(nums)
    currentStreak = 0
    longestStreak = 0
    
    for num in numSet:
        if (num - 1) not in numSet:
            currentNum = num
            currentStreak = 1
            
            while (currentNum + 1) in numSet:
                currentNum += 1
                currentStreak += 1
                
        longestStreak = max(longestStreak, currentStreak)
    return longestStreak

# Examples
nums1 = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums1)) # Output: 4

# New examples
nums2 = [1, 2, 0, 1]
print(longestConsecutive(nums2)) # Output: 3

nums3 = [0, 1, 2, 3, 4, 5]
print(longestConsecutive(nums3)) # Output: 6

nums4 = [10, 5, 1, 2, 3, 4, 6, 7, 8, 9]
print(longestConsecutive(nums4)) # Output: 9

nums5 = [8, 7, 6, 5, 4, 3, 2, 1]
print(longestConsecutive(nums5)) # Output: 8

nums6 = [1, 3, 5, 7, 9]
print(longestConsecutive(nums6)) # Output: 1

nums7 = [100, 200, 300, 400]
print(longestConsecutive(nums7)) # Output: 1

nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(longestConsecutive(nums8)) # Output: 10

nums9 = [5, 6, 7, 8, 9, 10, 11, 12]
print(longestConsecutive(nums9)) # Output: 8

nums10 = [1, 2, 3, 5, 6, 7, 8]
print(longestConsecutive(nums10)) # Output: 4