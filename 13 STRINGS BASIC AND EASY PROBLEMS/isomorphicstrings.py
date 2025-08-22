# ISOMORPHIC STRINGS

'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''

def isomorphicStrings(s, t):
    map1, map2 = {}, {}
    
    for i in range(len(s)):
        char1,  char2 = s[i], t[i]
        
        if char1 in map1 and map1[char1] != char2: 
            return False
        
        if char2 in map2 and map2[char2] != char1:
            return False
        
        map1[char1] = char2
        map2[char2] = char1
        
    return True

# Examples
s1 = "egg", t1 = "add"
print(isomorphicStrings(s1, t1)) # Output: True

# Additional examples
s2 = "foo", t2 = "bar"
print(isomorphicStrings(s2, t2)) # Output: False

s3 = "paper", t3 = "title"
print(isomorphicStrings(s3, t3)) # Output: True

s4 = "badc", t4 = "baba"
print(isomorphicStrings(s4, t4)) # Output: False

s5 = "a", t5 = "b"
print(isomorphicStrings(s5, t5)) # Output: True

s6 = "ab", t6 = "aa"
print(isomorphicStrings(s6, t6)) # Output: False

s7 = "hello", t7 = "world"
print(isomorphicStrings(s7, t7)) # Output: False

s8 = "abc", t8 = "def"
print(isomorphicStrings(s8, t8)) # Output: True

s9 = "aa", t9 = "bb"
print(isomorphicStrings(s9, t9)) # Output: True

s10 = "ab", t10 = "cd"
print(isomorphicStrings(s10, t10)) # Output: True