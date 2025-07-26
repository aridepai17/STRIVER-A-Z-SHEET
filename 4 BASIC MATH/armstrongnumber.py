# CHECK IF THE NUMBER IS ARMSTRONG OR NOT 

'''
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.
'''

def isArmstrong(n):
  k = len(str(n))
  sum = 0
  num = n
  
  while n > 0:
    lastDigit = n % 10
    sum += lastDigit ** k
    n = n // 10
    
    return sum == num
  
# Examples 
n1 = 0
print(f"Is {n1} an Armstrong number? {isArmstrong(n1)}")  # Output: True

n2 = 1
print(f"Is {n2} an Armstrong number? {isArmstrong(n2)}")  # Output: True

n3 = 2
print(f"Is {n3} an Armstrong number? {isArmstrong(n3)}")  # Output: True

n4 = 3
print(f"Is {n4} an Armstrong number? {isArmstrong(n4)}")  # Output: True

n5 = 4
print(f"Is {n5} an Armstrong number? {isArmstrong(n5)}")  # Output: True

n6 = 5
print(f"Is {n6} an Armstrong number? {isArmstrong(n6)}")  # Output: True

n7 = 6
print(f"Is {n7} an Armstrong number? {isArmstrong(n7)}")  # Output: True

n8 = 7
print(f"Is {n8} an Armstrong number? {isArmstrong(n8)}")  # Output: True

n9 = 153
print(f"Is {n9} an Armstrong number? {isArmstrong(n9)}")  # Output: True (1^3 + 5^3 + 3^3 = 153)

n10 = 370
print(f"Is {n10} an Armstrong number? {isArmstrong(n10)}")  # Output: True (3^3 + 7^3 + 0^3 = 370)

n11 = 371
print(f"Is {n11} an Armstrong number? {isArmstrong(n11)}")  # Output: True (3^3 + 7^3 + 1^3 = 371)

n12 = 9474
print(f"Is {n12} an Armstrong number? {isArmstrong(n12)}")  # Output: True (9^4 + 4^4 + 7^4 + 4^4 = 9474)

n13 = 123
print(f"Is {n13} an Armstrong number? {isArmstrong(n13)}")  # Output: False (1^3 + 2^3 + 3^3 != 123)

n14 = 100
print(f"Is {n14} an Armstrong number? {isArmstrong(n14)}")  # Output: False (1^3 + 0^3 + 0^3 != 100) 