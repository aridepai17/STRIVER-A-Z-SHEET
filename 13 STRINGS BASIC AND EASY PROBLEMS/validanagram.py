# VALID ANAGRAM

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def validAnagram(s, t):
    return sorted(s) == sorted(t) # One Line Answer

def validAnagram1(s, t):
    freq1 = {}
    freq2 = {}
    
    m = len(s)
    n = len(t)
    
    for i in range(m):
        if s[i] in freq1:
            freq1[s[i]] += 1
        else:
            freq1[s[i]] = 1
            
    for i in range(n):
        if t[i] in freq2:
            freq2[t[i]] += 1
        else:
            freq2[t[i]] = 1
            
    return freq1 == freq2

# Examples
s1 = "anagram", t1 = "nagaram"
print(validAnagram(s1, t1)) # Output: True

# 2. Same strings (True)
s2 = "abc"; t2 = "abc"
print(validAnagram(s2, t2))  # True

# 3. Different lengths (False)
s3 = "ab"; t3 = "aab"
print(validAnagram(s3, t3))  # False

# 4. Case sensitivity (False: 'L' != 'l')
s4 = "Listen"; t4 = "Silent"
print(validAnagram(s4, t4))  # False

# 5. Empty strings (True)
s5 = ""; t5 = ""
print(validAnagram(s5, t5))  # True

# 6. Single character (True)
s6 = "z"; t6 = "z"
print(validAnagram(s6, t6))  # True

# 7. Repeated characters (True)
s7 = "aabbcc"; t7 = "baccab"
print(validAnagram(s7, t7))  # True

# 8. Repeated characters but different counts (False)
s8 = "aabbc"; t8 = "abbcc"
print(validAnagram(s8, t8))  # False

# 9. Numeric characters (True)
s9 = "112233"; t9 = "332211"
print(validAnagram(s9, t9))  # True

# 10. With punctuation (True)
s10 = "a!b?c"; t10 = "c?b!a"
print(validAnagram(s10, t10))  # True

# 11. Longer string (True)
s11 = "thequickbrownfox"; t11 = "xofnworbkciuqeht"
print(validAnagram(s11, t11))  # True