# LEFT ROTATE ARRAY BY K PLACES 

# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

def leftRotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[k:] + nums[:k]
    return nums

# Examples 
nums1 = [1, 2, 3, 4, 5, 6]
k1 = 2
print(leftRotate(nums1, k1))  # Should print [3, 4, 5, 6, 1, 2]

nums2 = [5, 6, 7, 8, 9]
k2 = 3
print(leftRotate(nums2, k2))  # Should print [8, 9, 5, 6, 7]

nums3 = [10, 20, 30, 40, 50]
k3 = 1
print(leftRotate(nums3, k3))  # Should print [20, 30, 40, 50, 10]

nums4 = [1]
k4 = 0
print(leftRotate(nums4, k4))  # Should print [1] (single element)

nums5 = []
k5 = 2
print(leftRotate(nums5, k5))  # Should print [] (empty array)

nums6 = [1, 2, 3, 4]
k6 = 4
print(leftRotate(nums6, k6))  # Should print [1, 2, 3, 4] (k equals length)

nums7 = [2, 4, 6, 8, 10]
k7 = 2
print(leftRotate(nums7, k7))  # Should print [6, 8, 10, 2, 4]

nums8 = [7, 5, 3, 9, 1]
k8 = 3
print(leftRotate(nums8, k8))  # Should print [9, 1, 7, 5, 3]

nums9 = [0, 1, 2, 3, 4]
k9 = 1
print(leftRotate(nums9, k9))  # Should print [1, 2, 3, 4, 0]

nums10 = [9, 8, 7, 6, 5]
k10 = 2
print(leftRotate(nums10, k10))  # Should print [7, 6, 5, 9, 8]