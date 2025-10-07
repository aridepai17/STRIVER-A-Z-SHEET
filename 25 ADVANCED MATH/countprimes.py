# COUNT PRIMES

# Given an integer n, return the number of prime numbers that are strictly less than n.

def countPrimes(n):
    if n < 2:
        return 0
    
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    
    i = 2
    while i * i < n:
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
                
        i += 1
                
    return sum(sieve)

'''
# Time Complexity: O(n * log(log(n)))
# The outer loop runs up to sqrt(n). The inner loop marks multiples of each prime number.
# The total number of marking operations is approximately n * (1/2 + 1/3 + 1/5 + ... + 1/p) where p <= sqrt(n).
# The sum of the reciprocals of primes up to a certain number x is approximately log(log(x)).
# Therefore, the time complexity of the sieving process is O(n * log(log(n))).
# The initialization and final sum take O(n), so the overall complexity is dominated by the sieving part.

# Space Complexity: O(n)
# We use a boolean array (list in Python) of size n to store whether each number is prime.
# The space required is directly proportional to the input n.
'''

# Test Cases
n1 = 10
print(countPrimes(n1)) # Output: 4

n2 = 0
print(countPrimes(n2)) # Output: 0

n3 = 1
print(countPrimes(n3)) # Output: 0

n4 = 2
print(countPrimes(n4)) # Output: 0

n5 = 3
print(countPrimes(n5)) # Output: 1

n6 = 25
print(countPrimes(n6)) # Output: 9 (2, 3, 5, 7, 11, 13, 17, 19, 23)

n7 = 100
print(countPrimes(n7)) # Output: 25

n8 = 49
print(countPrimes(n8)) # Output: 15

n9 = 1
print(countPrimes(n9)) # Output: 0

n10 = 13
print(countPrimes(n10)) # Output: 5 (2, 3, 5, 7, 11)