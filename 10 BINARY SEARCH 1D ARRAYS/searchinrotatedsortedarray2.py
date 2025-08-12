# SEARCH IN ROTATED SORTED ARRAY 2

'''
Given a sorted and rotated array arr[] and a target key. 
Check whether the key is present in the array or not.
Note: The array may contains duplicate elements.
'''

def searchinRotatedSortedArray2(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        if nums[left] == nums[mid] == nums[left]:
            left += 1
            right -= 1
            continue
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return False


# Examples
nums1 = [3, 3, 3, 1, 2, 3]
target1 = 3
print(searchinRotatedSortedArray2(nums1, target1)) # Output: True

# Additional examples
nums2 = [3, 3, 3, 1, 2, 3]
target2 = 1
print(searchinRotatedSortedArray2(nums2, target2)) # Output: True

nums3 = [1, 1, 1, 1, 1]
target3 = 1
print(searchinRotatedSortedArray2(nums3, target3)) # Output: True

nums4 = [1, 1, 1, 1, 1]
target4 = 2
print(searchinRotatedSortedArray2(nums4, target4)) # Output: False

nums5 = [2, 5, 6, 0, 0, 1, 2]
target5 = 0
print(searchinRotatedSortedArray2(nums5, target5)) # Output: True

nums6 = [2, 5, 6, 0, 0, 1, 2]
target6 = 3
print(searchinRotatedSortedArray2(nums6, target6)) # Output: False

nums7 = [1, 3, 1, 1, 1]
target7 = 3
print(searchinRotatedSortedArray2(nums7, target7)) # Output: True

nums8 = [1, 1, 1, 1, 1, 1, 1]
target8 = 0
print(searchinRotatedSortedArray2(nums8, target8)) # Output: False

nums9 = [4, 5, 6, 7, 0, 1, 2]
target9 = 5
print(searchinRotatedSortedArray2(nums9, target9)) # Output: True

nums10 = [4, 5, 6, 7, 0, 1, 2]
target10 = 8
print(searchinRotatedSortedArray2(nums10, target10)) # Output: False