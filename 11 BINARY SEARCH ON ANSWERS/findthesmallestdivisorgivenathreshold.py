# FIND THE SMALLEST DIVISORT GIVEN A THRESHOLD

'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
Each result of the division is rounded to the nearest integer greater than or equal to that element. 
(For example: 7/3 = 3 and 10/2 = 5).
The test cases are generated so that there will be an answer.
'''

def smallestDivisort(nums, threshold):
    left = 1
    right = max(nums)
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        currentSum = 0
        
        for num in nums:
            currentSum += (num + mid - 1) // mid 
            
        if currentSum <= threshold:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return result


# Examples
nums1, threshold1 = [1,2,5,9], 6
print(smallestDivisort(nums1, threshold1)) # Output: 5

nums2, threshold2 = [44,22,33,11,1], 5
print(smallestDivisort(nums2, threshold2)) # Output: 44

nums3, threshold3 = [1,2,3,4,5], 10
print(smallestDivisort(nums3, threshold3)) # Output: 1

nums4, threshold4 = [1,2,3,4,5], 5
print(smallestDivisort(nums4, threshold4)) # Output: 3

nums5, threshold5 = [10,10,10,10], 4
print(smallestDivisort(nums5, threshold5)) # Output: 10

nums6, threshold6 = [10,10,10,10], 5
print(smallestDivisort(nums6, threshold6)) # Output: 8

nums7, threshold7 = [1,1,1,1], 4
print(smallestDivisort(nums7, threshold7)) # Output: 1

nums8, threshold8 = [1,1,1,1], 2
print(smallestDivisort(nums8, threshold8)) # Output: 2

nums9, threshold9 = [100,50,25], 3
print(smallestDivisort(nums9, threshold9)) # Output: 100

nums10, threshold10 = [100,50,25], 4
print(smallestDivisort(nums10, threshold10)) # Output: 75

nums11, threshold11 = [2,3,5,7,11], 11
print(smallestDivisort(nums11, threshold11)) # Output: 3

nums12, threshold12 = [8,4,2,1], 8
print(smallestDivisort(nums12, threshold12)) # Output: 2

nums13, threshold13 = [15,10,5,3], 6
print(smallestDivisort(nums13, threshold13)) # Output: 8

nums14, threshold14 = [20,15,10,5], 12
print(smallestDivisort(nums14, threshold14)) # Output: 6

nums15, threshold15 = [1,2,3,4,5,6,7,8,9,10], 15
print(smallestDivisort(nums15, threshold15)) # Output: 3