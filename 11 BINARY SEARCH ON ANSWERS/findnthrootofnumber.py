# FIND NTH ROOT OF NUMBER 

'''
You are given 2 numbers n and m, the task is to find n√m (nth root of m). 
If the root is not integer then returns -1.
'''

def nthRoot(n, m):
    if m == 0:
        return 0
    if m == 1:
        return 1
    
    left = 1
    right = m

    while left <= right:
        mid = (left + right) // 2
        
        midPower = mid ** n
        
        if midPower == m:
            return mid
        elif midPower < m:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Examples
n1, m1 = 3, 27
print(nthRoot(n1, m1)) # Output: 3

n2, m2 = 2, 4
print(nthRoot(n2, m2)) # Output: 2

n3, m3 = 2, 8
print(nthRoot(n3, m3)) # Output: -1

n4, m4 = 3, 64
print(nthRoot(n4, m4)) # Output: 4

n5, m5 = 4, 16
print(nthRoot(n5, m5)) # Output: 2

n6, m6 = 5, 32
print(nthRoot(n6, m6)) # Output: 2

n7, m7 = 4, 81
print(nthRoot(n7, m7)) # Output: 3

n8, m8 = 5, 243
print(nthRoot(n8, m8)) # Output: 3

n9, m9 = 10, 1024
print(nthRoot(n9, m9)) # Output: 2

n10, m10 = 7, 0
print(nthRoot(n10, m10)) # Output: 0

n11, m11 = 6, 1000000000000
print(nthRoot(n11, m11)) # Output: 100