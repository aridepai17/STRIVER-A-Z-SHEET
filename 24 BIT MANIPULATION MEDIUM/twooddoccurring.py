# TWO ODD OCCURRING

'''
Given an unsorted array, arr[] of positive numbers that contains even number of occurrences for all numbers except two numbers. 
Return that two numbers in decreasing order which has odd occurrences.
'''

def twoOddNum(arr):
    xorSum = 0
    
    for num in arr:
        xorSum ^= num
        
    rightmostSetBit = xorSum ^ -xorSum
    
    num1 = 0
    num2 = 0
    
    for num in arr:
        if num & rightmostSetBit:
            num1 ^= num
        else:
            num2 ^= num
            
    if num1 >= num2:
        return num2, num1
    else:
        return num1, num2

'''
Time Complexity: O(n)
The algorithm iterates through the input array `arr` twice.
The first loop calculates the XOR sum of all elements, which takes O(n) time, where n is the number of elements in the array.
The second loop partitions the elements into two groups based on the rightmost set bit of the XOR sum and calculates the XOR for each group. This also takes O(n) time.
Since the loops are sequential, the total time complexity is O(n) + O(n) = O(n).

Space Complexity: O(1)
The algorithm uses a few constant-size variables (`xorSum`, `rightmostSetBit`, `num1`, `num2`) to store intermediate values.
The space required does not scale with the size of the input array. Therefore, the space complexity is O(1).
'''

# Test Cases
arr1 = [4, 2, 4, 5, 2, 3, 3, 1]
print(twoOddNum(arr1)) # Output: 5, 1

arr2 = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]
print(twoOddNum(arr2)) # Output: 6, 3

arr3 = [10, 20]
print(twoOddNum(arr3)) # Output: 20, 10

arr4 = [8, 8, 7, 7, 6, 6, 1, 2]
print(twoOddNum(arr4)) # Output: 2, 1

arr5 = [100, 100, 100, 200, 200, 300]
print(twoOddNum(arr5)) # Output: 300, 100

arr6 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
print(twoOddNum(arr6)) # Output: 6, 5

arr7 = [12, 12, 1, 1, 1, 1, 2, 3, 3, 3]
print(twoOddNum(arr7)) # Output: 3, 2

arr8 = [5, 9]
print(twoOddNum(arr8)) # Output: 9, 5

arr9 = [2, 3, 4, 5, 2, 3, 4, 6]
print(twoOddNum(arr9)) # Output: 6, 5

arr10 = [1000, 500, 1000, 500, 1000, 200]
print(twoOddNum(arr10)) # Output: 1000, 200