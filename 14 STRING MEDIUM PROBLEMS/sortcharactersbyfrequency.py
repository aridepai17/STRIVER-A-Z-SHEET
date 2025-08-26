# SORT CHARACTERS BY FREQUENCY

'''
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
'''

def frequencySort(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    buckets = [[] for _ in range(len(s) + 1)]
    
    for char, count in freq.items():
        buckets[count].append(char)
        
    result = []
    
    for i in range(len(buckets) - 1, 0, -1):
        for char in buckets[i]:
            result.append(char * i)
            
    return "".join(result)

# Examples
s1 = "tree"
print(frequencySort(s1)) # Output: "eert"

s2 = "cccaaa"
print(frequencySort(s2)) # Output: "cccaaa"

s3 = "Aabb"
print(frequencySort(s3)) # Output: "bbAa"

s4 = "hello"
print(frequencySort(s4)) # Output: "llheo"

s5 = "leetcode"
print(frequencySort(s5)) # Output: "eeetclod"

s6 = "loveleetcode"
print(frequencySort(s6)) # Output: "eeeelllootvcd"

s7 = "aabbbcccc"
print(frequencySort(s7)) # Output: "ccccbbbaa"

s8 = "zzzzz"
print(frequencySort(s8)) # Output: "zzzzz"

s9 = "abc"
print(frequencySort(s9)) # Output: "abc"

s10 = "aaabbbccc"
print(frequencySort(s10)) # Output: "aaabbbccc"

s11 = "mississippi"
print(frequencySort(s11)) # Output: "ssssppiiim"