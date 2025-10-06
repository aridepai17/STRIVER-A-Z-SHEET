# ALL DIVISORS OF A NUMBER

# Given an integer n, print all the divisors of N in the ascending order.

def printDivisors(n):
    divisors = []
    limit = int(n ** 0.5)
    
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            complementaryDivisor = n // i
            if complementaryDivisor != i:
                divisors.append(complementaryDivisor)
                
    divisors.sort()
    return divisors

'''
Time Complexity: O(sqrt(n))
The algorithm's main component is a loop that runs from 1 to `sqrt(n)`. This part of the algorithm has a time complexity of O(sqrt(n)).
After finding the divisors, the list is sorted. If `d` is the number of divisors, sorting takes O(d * log d) time.
The loop is the dominant operation, so the total time complexity is effectively O(sqrt(n)).

Space Complexity: O(d), where d is the number of divisors
The space complexity is determined by the storage required for the `divisors` list.
The list stores all `d` divisors of the number `n`.
Thus, the space complexity is O(d).
'''

# Test Cases
n1 = 20
print(printDivisors(n1)) # Output: [1, 2, 4, 5, 10, 20]

n2 = 36
print(printDivisors(n2)) # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]

n3 = 13
print(printDivisors(n3)) # Output: [1, 13]

n4 = 100
print(printDivisors(n4)) # Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]

n5 = 1
print(printDivisors(n5)) # Output: [1]

n6 = 7
print(printDivisors(n6)) # Output: [1, 7]

n7 = 12
print(printDivisors(n7)) # Output: [1, 2, 3, 4, 6, 12]

n8 = 99
print(printDivisors(n8)) # Output: [1, 3, 9, 11, 33, 99]

n9 = 48
print(printDivisors(n9)) # Output: [1, 2, 3, 4, 6, 8, 12, 16, 24, 48]

n10 = 15
print(printDivisors(n10)) # Output: [1, 3, 5, 15]