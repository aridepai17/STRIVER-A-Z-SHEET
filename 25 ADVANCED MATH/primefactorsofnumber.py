# PRIME FACTORS OF A NUMBER

# Given a number n. Find its unique prime factors in increasing order.

def primeFac(n):
    primes = []
    limit = int(n ** 0.5)
    
    for i in range(2, limit + 1):
        if n % i == 0:
            primes.append(i)
            while n % i == 0:
                n //= i
                
    if n > 1:
        primes.append(n)
        
    return primes

'''
Time Complexity: O(sqrt(n))
The algorithm iterates from 2 up to the square root of n.
The outer loop runs `sqrt(n)` times.
Inside the loop, the `while` loop divides `n` by its prime factors. The total number of divisions across all iterations is at most O(log n), which is less significant than `sqrt(n)`.
Therefore, the dominant factor for the time complexity is the outer loop, making it O(sqrt(n)).

Space Complexity: O(log n)
The space complexity is determined by the `primes` list, which stores the unique prime factors of `n`.
The maximum number of unique prime factors for a number `n` is bounded by O(log n). For instance, the smallest number with `k` distinct prime factors is the product of the first `k` primes. This product grows very rapidly.
Thus, the space required to store the factors is proportional to log n.
'''

# Test Cases
n1 = 100
print(primeFac(n1)) # Output: [2, 5]

n2 = 12
print(primeFac(n2)) # Output: [2, 3]

n3 = 13
print(primeFac(n3)) # Output: [13]

n4 = 315
print(primeFac(n4)) # Output: [3, 5, 7]

n5 = 84
print(primeFac(n5)) # Output: [2, 3, 7]

n6 = 2
print(primeFac(n6)) # Output: [2]

n7 = 99
print(primeFac(n7)) # Output: [3, 11]

n8 = 1
print(primeFac(n8)) # Output: []

n9 = 49
print(primeFac(n9)) # Output: [7]

n10 = 210
print(primeFac(n10)) # Output: [2, 3, 5, 7]