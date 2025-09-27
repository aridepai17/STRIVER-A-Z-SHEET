# CONVERT NUMBER TO BINARY

'''
Given a non-negative integer `n`, write a function to return its binary representation as a string.
The returned string should not have leading zeros, except for the number 0 itself.
'''

def tobinaryString(n):
    binaryArray = []
    
    while n > 0:
        bit = n % 2
        binaryArray.append(bit)
        n //= 2
        
    binaryArray.reverse()
    return "".join(binaryArray)

'''
Time Complexity: O(log n)
The while loop runs as long as n is greater than 0. In each iteration, n is divided by 2.
The number of iterations is therefore proportional to log₂(n).
The operations inside the loop are constant time.
The `reverse()` and `join()` operations also take time proportional to the number of bits, which is log₂(n).
Thus, the overall time complexity is O(log n).

Space Complexity: O(log n)
We use an array, `binaryArray`, to store the bits of the number.
The number of bits in the binary representation of n is proportional to log₂(n).
Therefore, the space required to store these bits in the array is O(log n).
'''

# Test Cases
n1 = 7
print(tobinaryString(n1)) # Output: 111

n2 = 0
print(tobinaryString(n2)) # Output: 0

n3 = 1
print(tobinaryString(n3)) # Output: 1

n4 = 2
print(tobinaryString(n4)) # Output: 10

n5 = 10
print(tobinaryString(n5)) # Output: 1010

n6 = 16
print(tobinaryString(n6)) # Output: 10000

n7 = 15
print(tobinaryString(n7)) # Output: 1111

n8 = 100
print(tobinaryString(n8)) # Output: 1100100

n9 = 255
print(tobinaryString(n9)) # Output: 11111111

n10 = 1024
print(tobinaryString(n10)) # Output: 10000000000