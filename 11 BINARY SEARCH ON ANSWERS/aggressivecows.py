# AGGRESSIVE COWS

'''
You are given an array with unique elements of stalls[], which denote the positions of stalls. 
You are also given an integer k which denotes the number of aggressive cows. 
The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.
'''

def aggressiveCows(stalls, k):
    def canPlaceCows(distance, stalls, k):
        cowCount = 1
        lastPlacedCow = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - lastPlacedCow >= distance:
                cowCount += 1
                lastPlacedCow = stalls[i]
                
            if cowCount == k:
                return True
            
        return False
    
    
    stalls.sort()
    
    left = 1
    right = stalls[-1] - stalls[0]
    
    while left <= right:
        mid = (left + right) // 2
        
        if canPlaceCows(mid, stalls,k):
            left = mid + 1
        else:
            right = mid - 1
            
    return right

# Examples
stalls1 = [0, 3, 4, 7, 10, 9]
k1 = 4
print(aggressiveCows(stalls1, k1)) # Output: 3

# Additional examples
stalls2 = [1, 2, 3, 4, 5]
k2 = 3
print(aggressiveCows(stalls2, k2)) # Output: 2

stalls3 = [1, 2, 8, 4, 9]
k3 = 3
print(aggressiveCows(stalls3, k3)) # Output: 3

stalls4 = [10, 1, 2, 7, 5]
k4 = 2
print(aggressiveCows(stalls4, k4)) # Output: 9

stalls5 = [0, 100]
k5 = 2
print(aggressiveCows(stalls5, k5)) # Output: 100

stalls6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k6 = 5
print(aggressiveCows(stalls6, k6)) # Output: 2

stalls7 = [4, 2, 1, 3, 6]
k7 = 2
print(aggressiveCows(stalls7, k7)) # Output: 5

stalls8 = [5, 17, 100, 11]
k8 = 2
print(aggressiveCows(stalls8, k8)) # Output: 95

stalls9 = [1, 3, 5, 7, 9]
k9 = 5
print(aggressiveCows(stalls9, k9)) # Output: 2

stalls10 = [1, 3, 5, 7, 9]
k10 = 4
print(aggressiveCows(stalls10, k10)) # Output: 2

stalls11 = [1, 2, 4, 8, 9]
k11 = 3
print(aggressiveCows(stalls11, k11)) # Output: 3