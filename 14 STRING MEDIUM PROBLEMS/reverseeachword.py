# REVERSE EACH WORD 

# You are given a string s. You need to reverse each word in it where the words are separated by spaces and return the modified string.

def reverseWords(s):
    words = s.split()
    result = []
    
    for word in words:
        word = word[::-1]
        result.append(word)
        
    return " ".join(result)

# Examples

s1 = "hello world"
print(reverseWords(s1)) # Output: "olleh dlrow"

s2 = "a b c"
print(reverseWords(s2)) # Output: "a b c"

s3 = "Let's code"
print(reverseWords(s3)) # Output: "s'teL edoc"

s4 = "  leading spaces"
print(reverseWords(s4)) # Output: "gnidael secaps"

s5 = "trailing spaces  "
print(reverseWords(s5)) # Output: "gniliart secaps"

s6 = "multiple   spaces here"
print(reverseWords(s6)) # Output: "elpitlum secaps ereh"

s7 = "123 456"
print(reverseWords(s7)) # Output: "321 654"

s8 = ""
print(reverseWords(s8)) # Output: ""

s9 = "Palindrome level noon"
print(reverseWords(s9)) # Output: "emordnilaP level noon"

s10 = "MixedCASE Words"
print(reverseWords(s10)) # Output: "ESACdexiM sdroW"