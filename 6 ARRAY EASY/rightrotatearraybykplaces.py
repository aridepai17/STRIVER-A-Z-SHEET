# RIGHT ROTATE AN ARRAY BY K PLACES 

# Given an integer array nums and a non-negative integer k, rotate the array to the right by k steps.

def rightRotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Examples 
nums1 = [1, 2, 3, 4, 5]
k1 = 2
print(rightRotate(nums1, k1))  # Should print [4, 5, 1, 2, 3]

nums2 = [5, 6, 7, 8, 9]
k2 = 3
print(rightRotate(nums2, k2))  # Should print [7, 8, 9, 5, 6]

nums3 = [10, 20, 30, 40, 50]
k3 = 1
print(rightRotate(nums3, k3))  # Should print [50, 10, 20, 30, 40]

nums4 = [1]
k4 = 0
print(rightRotate(nums4, k4))  # Should print [1] (single element)

nums5 = []
k5 = 2
print(rightRotate(nums5, k5))  # Should print [] (empty array)

nums6 = [1, 2, 3, 4]
k6 = 4
print(rightRotate(nums6, k6))  # Should print [1, 2, 3, 4] (k equals length)

nums7 = [2, 4, 6, 8, 10]
k7 = 2
print(rightRotate(nums7, k7))  # Should print [8, 10, 2, 4, 6]

nums8 = [7, 5, 3, 9, 1]
k8 = 3
print(rightRotate(nums8, k8))  # Should print [5, 3, 9, 1, 7]

nums9 = [0, 1, 2, 3, 4]
k9 = 1
print(rightRotate(nums9, k9))  # Should print [4, 0, 1, 2, 3]

nums10 = [9, 8, 7, 6, 5]
k10 = 2
print(rightRotate(nums10, k10))  # Should print [6, 5, 9, 8, 7]