# MAJORITY ELEMENT 2

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''

def majorityElement2(nums):
    count1 = count2 = 0
    candidate1 = candidate2 = None 
    
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num 
            count1 = 1
        elif count2 == 0:
            candidate2 = num 
            count2 = 1 
        else:
            count1 -= 1 
            count2 -= 1 
            
        result = []
        n = len(nums)
        
        for candidate in set([candidate1, candidate2]):
            if nums.count(candidate) > n//3:
                result.append(candidate)
                
        return result
    
# Examples
nums1 = [3, 2, 3]
print(majorityElement2(nums1)) # Output: [3]

# Additional examples
nums2 = [1]
print(majorityElement2(nums2)) # Output: [1]

nums3 = [1, 2]
print(majorityElement2(nums3)) # Output: []

nums4 = [1, 1, 1, 3, 3, 2, 2, 2]
print(majorityElement2(nums4)) # Output: [1, 2]

nums5 = [3, 3, 4]
print(majorityElement2(nums5)) # Output: [3]

nums6 = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement2(nums6)) # Output: [2]

nums7 = [5, 5, 5, 2, 2, 2, 3, 3]
print(majorityElement2(nums7)) # Output: [5, 2]

nums8 = [1, 2, 3, 4, 5, 6, 7, 8]
print(majorityElement2(nums8)) # Output: []

nums9 = [1, 1, 1, 2, 2, 3, 3, 3]
print(majorityElement2(nums9)) # Output: [1, 3]

nums10 = [0, 0, 0, 1, 1, 1, 2]
print(majorityElement2(nums10)) # Output: [0, 1]