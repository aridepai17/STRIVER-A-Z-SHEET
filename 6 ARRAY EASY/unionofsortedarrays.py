# UNION OF SORTED ARRAYS 

'''
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays.
The elements in the union must be in ascending order.
The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.
'''

def findUnion(a, b):
    left, right = 0, 0
    m, n = len(a), len(b)
    union = []
    
    while left < m and right < n:
        if a[left] <= b[right]:
            if len(union) == 0 or union[-1] != a[left]:
                union.append(a[left])
            left += 1
        else:
            if len(union) == 0 or union[-1] != b[right]:
                union.append(b[right])
            right += 1
            
    while left < m:
        if union[-1] != a[left]:
            union.append(a[left])
        left += 1
        
    while right < n:
        if union[-1] != b[right]:
            union.append(b[right])
        right += 1
        
    return union

# Examples 

a1 = [1, 2, 3, 4, 5], b1 = [1, 2, 3, 6, 7]
print(findUnion(a1, b1)) # Output: [1, 2, 3, 4, 5, 6, 7]

# Additional Examples
a2, b2 = [1, 2, 3], [2, 3, 4]
print(f"findUnion({a2}, {b2}) = {findUnion(a2, b2)}")  # Output: [1, 2, 3, 4]

a3, b3 = [1, 3, 5], [2, 4, 6]
print(f"findUnion({a3}, {b3}) = {findUnion(a3, b3)}")  # Output: [1, 2, 3, 4, 5, 6]

a4, b4 = [1, 2, 3], []
print(f"findUnion({a4}, {b4}) = {findUnion(a4, b4)}")  # Output: [1, 2, 3]

a5, b5 = [], [4, 5, 6]
print(f"findUnion({a5}, {b5}) = {findUnion(a5, b5)}")  # Output: [4, 5, 6]

a6, b6 = [1, 1, 2], [2, 3, 4]
print(f"findUnion({a6}, {b6}) = {findUnion(a6, b6)}")  # Output: [1, 2, 3, 4]

a7, b7 = [5, 6, 7], [1, 2, 3]
print(f"findUnion({a7}, {b7}) = {findUnion(a7, b7)}")  # Output: [1, 2, 3, 5, 6, 7]

a8, b8 = [1, 2, 2, 3], [2, 3, 4]
print(f"findUnion({a8}, {b8}) = {findUnion(a8, b8)}")  # Output: [1, 2, 3, 4]

a9, b9 = [1, 2, 3], [1, 2, 3]
print(f"findUnion({a9}, {b9}) = {findUnion(a9, b9)}")  # Output: [1, 2, 3]

a10, b10 = [1, 2, 3, 4], [5, 6, 7]
print(f"findUnion({a10}, {b10}) = {findUnion(a10, b10)}")  # Output: [1, 2, 3, 4, 5, 6, 7]

a11, b11 = [1, 2], [3, 4, 5, 6]
print(f"findUnion({a11}, {b11}) = {findUnion(a11, b11)}")  # Output: [1, 2, 3, 4, 5, 6]