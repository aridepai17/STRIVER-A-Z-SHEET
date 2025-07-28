# HIGHEST OCCURRING ELEMENT IN AN ARRAY

'''
Given an array of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. 
If there are multiple elements that appear a maximum number of times, find the smallest of them.
'''

def mostFrequentElement(nums):
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    maxFreq = max(freq.values())
            
    candidates = []
    for num in freq:
        if freq[num] == maxFreq:
            candidates.append(num)
            
    return min(candidates)

# Examples
nums1 = [1, 2, 2, 3, 3, 3]
print(mostFrequentElement(nums1))  # Should print 3

nums2 = [4, 4, 4, 1, 1, 2]
print(mostFrequentElement(nums2))  # Should print 4

nums3 = [5, 5, 5, 2, 2, 1]
print(mostFrequentElement(nums3))  # Should print 5

nums4 = [1, 1, 2, 2, 3, 3]
print(mostFrequentElement(nums4))  # Should print 1 (smallest of the most frequent)

nums5 = [7, 8, 8, 9, 9, 9]
print(mostFrequentElement(nums5))  # Should print 9

nums6 = [10, 10, 10, 10, 5, 5, 5]
print(mostFrequentElement(nums6))  # Should print 10

nums7 = [1, 2, 3, 4, 5]
print(mostFrequentElement(nums7))  # Should print 1 (all unique, smallest is 1)

nums8 = [0, 0, 0, 1, 1, 2, 2]
print(mostFrequentElement(nums8))  # Should print 0

nums9 = [3, 3, 3, 2, 2, 1, 1, 1]
print(mostFrequentElement(nums9))  # Should print 3

nums10 = [6, 6, 6, 7, 7, 7, 8]
print(mostFrequentElement(nums10))  # Should print 6 (both 6 and 7 appear 3 times, but 6 is smaller)
