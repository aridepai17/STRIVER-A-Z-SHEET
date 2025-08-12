# COUNT OCCURRENCES IN SORTED ARRAY

'''
You are given a sorted array of integers arr and an integer target. 
Your task is to determine how many times target appears in arr.
Return the count of occurrences of target in the array.
'''

def findFirst(nums, target):
    left = 0
    right = len(nums) - 1
    first = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            if nums[mid] == target:
                first = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return first

def findLast(nums, target):
    left = 0
    right = len(nums) - 1
    last = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            if nums[mid] == target:
                last = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return last

def countOccurrencesinSortedArray(nums, target):
    firstIndex = findFirst(nums, target)
    lastIndex = findLast(nums, target)
    
    if firstIndex == -1:
        return 0
    
    return lastIndex - firstIndex + 1


# Examples
nums1 = [0, 0, 1, 1, 1, 2, 3]
target1 = 1
print(countOccurrencesinSortedArray(nums1, target1)) # Output: 3

# Additional examples
nums2 = [1, 2, 2, 3, 4, 5]
target2 = 2
print(countOccurrencesinSortedArray(nums2, target2)) # Output: 2

nums3 = [1, 1, 1, 1, 1]
target3 = 1
print(countOccurrencesinSortedArray(nums3, target3)) # Output: 5

nums4 = [1, 2, 3, 4, 5]
target4 = 6
print(countOccurrencesinSortedArray(nums4, target4)) # Output: 0

nums5 = [10, 20, 30, 40, 50]
target5 = 25
print(countOccurrencesinSortedArray(nums5, target5)) # Output: 0

nums6 = [1, 3, 5, 7, 9]
target6 = 3
print(countOccurrencesinSortedArray(nums6, target6)) # Output: 1

nums7 = [1, 2, 3, 4, 5]
target7 = 1
print(countOccurrencesinSortedArray(nums7, target7)) # Output: 1

nums8 = [1, 2, 3, 4, 5]
target8 = 5
print(countOccurrencesinSortedArray(nums8, target8)) # Output: 1

nums9 = [1, 2, 2, 3, 4, 5]
target9 = 3
print(countOccurrencesinSortedArray(nums9, target9)) # Output: 1

nums10 = [5, 5, 5, 5, 5]
target10 = 5
print(countOccurrencesinSortedArray(nums10, target10)) # Output: 5