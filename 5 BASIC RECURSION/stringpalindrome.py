# STRING PALINDROME 

'''
Given a string s, return true if the string is palindrome, otherwise false.
A string is called palindrome if it reads the same forward and backward.
'''

# NOT RECURSIVE 

def palindromeCheck(s):
  left, right = 0, len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True 

# Examples
print(palindromeCheck("racecar"))      # Should print True
print(palindromeCheck("madam"))        # Should print True
print(palindromeCheck("hello"))        # Should print False
print(palindromeCheck("A man a plan a canal Panama"))  # Should print False (case-sensitive)
print(palindromeCheck("12321"))        # Should print True
print(palindromeCheck("12345"))        # Should print False
print(palindromeCheck("Able was I ere I saw Elba"))  # Should print False (case-sensitive)
print(palindromeCheck("noon"))         # Should print True
print(palindromeCheck("civic"))        # Should print True
print(palindromeCheck("deified"))      # Should print True