# ROTATE STRING

'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
'''

def rotateString(s, goal):
    return len(s) == len(goal) and goal in s + s


# Examples
# 1. Basic rotation (True)
s1 = "abcde"; goal1 = "cdeab"
print(rotateString(s1, goal1))  # True

# 2. Not a rotation (False)
s2 = "abcde"; goal2 = "abced"
print(rotateString(s2, goal2))  # False

# 3. All same characters (True)
s3 = "aaaa"; goal3 = "aaaa"
print(rotateString(s3, goal3))  # True

# 4. Same string (0 shifts, True)
s4 = "abc"; goal4 = "abc"
print(rotateString(s4, goal4))  # True

# 5. Rotation by one (True)
s5 = "abc"; goal5 = "bca"
print(rotateString(s5, goal5))  # True

# 6. Anagram but not rotation (False)
s6 = "abc"; goal6 = "acb"
print(rotateString(s6, goal6))  # False

# 7. Empty strings (True)
s7 = ""; goal7 = ""
print(rotateString(s7, goal7))  # True

# 8. Single character (True)
s8 = "a"; goal8 = "a"
print(rotateString(s8, goal8))  # True

# 9. Two characters swapped (True)
s9 = "ab"; goal9 = "ba"
print(rotateString(s9, goal9))  # True

# 10. Classic rotation example (True)
s10 = "waterbottle"; goal10 = "erbottlewat"
print(rotateString(s10, goal10))  # True