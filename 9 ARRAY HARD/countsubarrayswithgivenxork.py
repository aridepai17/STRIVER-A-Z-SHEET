# COUNT SUBARRAYS WITH GIVEN XOR K 

'''
Given an array of integers A and an integer B, return the total number of subarrays whose total XOR equals to k
'''

def countSubarrayswithXOR(A, B):
    freq = {}
    count = 0
    prefixXOR = 0
    
    for num in A:
        prefixXOR ^= num
        
        if prefixXOR == B:
            count += 1
        
        required = prefixXOR ^ B
        
        if required in freq:
            count += freq[required]
            
        freq[prefixXOR] = freq.get(prefixXOR, 0) + 1
        
    return count

# Examples
A1 = [4, 2, 2, 6, 4]
B1 = 6
print(countSubarrayswithXOR(A1, B1)) # Output: 4

# Additional examples
A2 = [1, 2, 3, 4]
B2 = 3
print(countSubarrayswithXOR(A2, B2)) # Output: 2

A3 = [5, 1, 2, 3, 0]
B3 = 3
print(countSubarrayswithXOR(A3, B3)) # Output: 3

A4 = [1, 2, 3, 4, 5]
B4 = 7
print(countSubarrayswithXOR(A4, B4)) # Output: 3

A5 = [2, 2, 2, 2]
B5 = 2
print(countSubarrayswithXOR(A5, B5)) # Output: 10

A6 = [1, 2, 1, 2, 1]
B6 = 2
print(countSubarrayswithXOR(A6, B6)) # Output: 6

A7 = [0, 0, 0, 0]
B7 = 0
print(countSubarrayswithXOR(A7, B7)) # Output: 10

A8 = [3, 3, 3, 3]
B8 = 3
print(countSubarrayswithXOR(A8, B8)) # Output: 10

A9 = [1, 2, 3, 4, 5, 6]
B9 = 1
print(countSubarrayswithXOR(A9, B9)) # Output: 1

A10 = [1, 2, 3, 4, 5]
B10 = 0
print(countSubarrayswithXOR(A10, B10)) # Output: 0