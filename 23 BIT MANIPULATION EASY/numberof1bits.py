# NUMBER OF 1 BITS

'''
Given a positive integer n. Your task is to return the count of set bits.
'''
# Solution 1: Brute Force
def setBits(n):
    count = 0
    
    while n > 0:
        remainder = n % 2
        if remainder == 1:
            count += 1
        n //= 2
        
    return count

'''
Time Complexity: O(log n)
The `while` loop iterates as many times as there are bits in the binary representation of `n`. For an integer `n`, the number of bits is approximately log2(n). Therefore, the time complexity is O(log n).

Space Complexity: O(1)
The function uses a constant amount of extra space (for the `count` variable), regardless of the size of the input `n`.
'''

# Solution 2: Using BitWise Operators
def setBits2(n):
    count = 0
    
    while n > 0:
        count += n & 1
        n = n >> 1
    
    return count

'''
Time Complexity: O(log n)
The `while` loop runs as long as `n` is greater than 0. In each iteration, `n` is right-shifted by 1, which is equivalent to dividing it by 2. This process continues until `n` becomes 0. The number of iterations is equal to the number of bits in the binary representation of `n`, which is approximately log2(n). Thus, the time complexity is O(log n).

Space Complexity: O(1)
The function uses a constant amount of extra space for the `count` variable. The space required does not depend on the size of the input `n`, making the space complexity constant.
'''

# Solution 3: Alternate Solution uisng BitWise Operators
def setBits3(n):
    count = 0
    
    while n > 0:
        n = n & (n - 1)
        count += 1
        
    return count

'''
Time Complexity: O(k) where k is the number of set bits
The `while` loop iterates as many times as there are set bits (1s) in the binary representation of `n`. The operation `n & (n - 1)` clears the rightmost set bit. Therefore, the loop runs `k` times, where `k` is the number of set bits. This is more efficient than O(log n) for numbers with a sparse number of set bits.

Space Complexity: O(1)
The function uses a constant amount of extra space for the `count` variable, regardless of the size of the input `n`.
'''
# Test Cases
n1 = 6
print(setBits(n1)) # Output: 2

n2 = 0
print(setBits(n2)) # Output: 0

n3 = 1
print(setBits(n3)) # Output: 1

n4 = 7
print(setBits(n4)) # Output: 3

n5 = 15
print(setBits(n5)) # Output: 4

n6 = 16
print(setBits(n6)) # Output: 1

n7 = 100
print(setBits(n7)) # Output: 3

n8 = 42
print(setBits(n8)) # Output: 3

n9 = 255
print(setBits(n9)) # Output: 8

n10 = 1023
print(setBits(n10)) # Output: 10