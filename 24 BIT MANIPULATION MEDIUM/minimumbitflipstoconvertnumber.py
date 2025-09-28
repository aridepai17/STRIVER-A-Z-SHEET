# MINIMUM BIT FLIPS TO CONVERT NUMBER

'''
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
'''

# Solution 1: Using In-Built Functions
def minBitFlips1(start, goal):
    answer = start ^ goal
    return bin(answer).count('1')

'''
Time Complexity: O(log N)
The time complexity is determined by the `bin()` function and the `.count()` method.
- `start ^ goal`: This is a constant time operation, O(1).
- `bin(answer)`: This converts the integer `answer` to its binary string representation. The length of this string is proportional to the number of bits in `answer`, which is O(log N), where N is the value of `answer`.
- `.count('1')`: This method iterates through the binary string to count the '1's. The time taken is proportional to the length of the string, which is O(log N).
Therefore, the overall time complexity is O(log N), where N is the maximum value between start and goal.

Space Complexity: O(log N)
The space complexity is determined by the storage required for the binary string representation of `answer`.
- The `bin(answer)` function creates a string whose length is proportional to the number of bits in `answer`, which is O(log N).
This is the dominant factor in space usage, so the space complexity is O(log N).
'''

# Solution 2: Using BitWise Operators and Traversal
def minBitFlips2(start, goal):
    answer = start ^ goal
    count = 0
    
    for i in range(32):
        if answer & (1 << i):
            count += 1
            
    return count

'''
Time Complexity: O(1)
The function iterates a fixed number of times (32), which corresponds to the number of bits in a standard 32-bit integer.
- `start ^ goal`: This is a constant time operation, O(1).
- The `for` loop runs exactly 32 times, regardless of the values of `start` and `goal`.
- Inside the loop, all operations (`&`, `<<`, `+`) are constant time bitwise and arithmetic operations.
Since the number of iterations is constant, the overall time complexity is O(1).

Space Complexity: O(1)
The function uses a fixed amount of extra space for variables like `answer`, `count`, and the loop counter `i`.
- The space required does not depend on the size of the input integers `start` and `goal`.
Therefore, the space complexity is O(1).
'''

# Test Cases
start1 = 10, goal1 = 7
print(minBitFlips2(start1, goal1)) # Output: 3

start2 = 3, goal2 = 4
print(minBitFlips2(start2, goal2)) # Output: 3

start3 = 0, goal3 = 0
print(minBitFlips2(start3, goal3)) # Output: 0

start4 = 15, goal4 = 0
print(minBitFlips2(start4, goal4)) # Output: 4

start5 = 20, goal5 = 25
print(minBitFlips2(start5, goal5)) # Output: 3

start6 = 123, goal6 = 456
print(minBitFlips2(start6, goal6)) # Output: 6

start7 = 7, goal7 = 7
print(minBitFlips2(start7, goal7)) # Output: 0

start8 = 1, goal8 = 16
print(minBitFlips2(start8, goal8)) # Output: 2

start9 = 88, goal9 = 19
print(minBitFlips2(start9, goal9)) # Output: 4

start10 = 1024, goal10 = 0
print(minBitFlips2(start10, goal10)) # Output: 1