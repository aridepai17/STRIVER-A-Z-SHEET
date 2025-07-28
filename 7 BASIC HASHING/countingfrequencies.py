# COUNTING FREQUENCIES OF  ARRAY ELEMENTS 

'''
Given an array nums of size n which may contain duplicate elements, return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
You may return the result in any order, but each element must appear exactly once in the output.
'''

def countFrequencies(nums):
    n = len(nums)
    freq = {}
    
    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq [nums[i]] = 1
            
        result = []
        
        for key in freq:
            result.append((key, freq[key]))
            
        return result