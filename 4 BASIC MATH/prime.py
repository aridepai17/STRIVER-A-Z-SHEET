# CHECK FOR PRIME NUMBER 

'''
You are given an integer n. You need to check if the number is prime or not. 
Return true if it is a prime number, otherwise return false.
A prime number is a number which has no divisors except 1 and itself.
'''
import math 

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

# Examples 
print(isPrime(1))   # False, 1 is not a prime number

print(isPrime(2))   # True, 2 is a prime number

print(isPrime(3))   # True, 3 is a prime number

print(isPrime(4))   # False, 4 is not a prime number

print(isPrime(5))   # True, 5 is a prime number

print(isPrime(6))   # False, 6 is not a prime number

print(isPrime(7))   # True, 7 is a prime number

print(isPrime(8))   # False, 8 is not a prime number

print(isPrime(9))   # False, 9 is not a prime number

print(isPrime(11))  # True, 11 is a prime number