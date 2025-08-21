# REVERSE WORDS IN A STRING

'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

def reverseWords(s):
    words = s.split()
    reversedWords = words[::-1]
    return " ".join(reversedWords) 

# Examples
s1 = "the sky is blue"
print(reverseWords(s1)) # Output: "blue is sky the"

# Additional examples
s2 = "  hello world  "
print(reverseWords(s2)) # Output: "world hello"

s3 = "a good   example"
print(reverseWords(s3)) # Output: "example good a"

s4 = "  Bob    Loves  Alice   "
print(reverseWords(s4)) # Output: "Alice Loves Bob"

s5 = "Alice does not even like bob"
print(reverseWords(s5)) # Output: "bob like even not does Alice"

s6 = "hello"
print(reverseWords(s6)) # Output: "hello"

s7 = "  hello  world  "
print(reverseWords(s7)) # Output: "world hello"

s8 = "the quick brown fox"
print(reverseWords(s8)) # Output: "fox brown quick the"

s9 = "   one   two   three   "
print(reverseWords(s9)) # Output: "three two one"

s10 = "programming is fun"
print(reverseWords(s10)) # Output: "fun is programming"