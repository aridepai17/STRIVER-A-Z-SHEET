# SUM OF BEAUTY OF ALL SUBSTRINGS 

'''
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
Given a string s, return the sum of beauty of all of its substrings.
'''

def beautySum(s):
    n = len(s)
    totalBeauty = 0
    
    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            frequencies = freq.values()
            
            maxFreq = max(frequencies)
            minFreq = min(frequencies)
            
            beautyValue = maxFreq - minFreq
            
            totalBeauty += beautyValue
            
    return totalBeauty

# Examples
s1 = "aabcb"
print(beautySum(s1)) # Output: 5

s2 = ""
print(beautySum(s2)) # Output: 0

s3 = "a"
print(beautySum(s3)) # Output: 0

s4 = "ab"
print(beautySum(s4)) # Output: 0

s5 = "aa"
print(beautySum(s5)) # Output: 0

s6 = "aab"
print(beautySum(s6)) # Output: 1

s7 = "abb"
print(beautySum(s7)) # Output: 1

s8 = "aabb"
print(beautySum(s8)) # Output: 2

s9 = "aba"
print(beautySum(s9)) # Output: 1

s10 = "abbc"
print(beautySum(s10)) # Output: 3

s11 = "aaabb"
print(beautySum(s11)) # Output: 5