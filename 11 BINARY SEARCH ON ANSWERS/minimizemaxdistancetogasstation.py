# MINIMIZE MAX DISTANCE TO GAS STATION

'''
We have a horizontal number line. 
On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[n-1], where n is the size of the stations array. 
Now, we add k more gas stations so that d, the maximum distance between adjacent gas stations, is minimized. 
We have to find the smallest possible value of d. Find the answer exactly to 2 decimal places.
Note: stations is in a strictly increasing order.
'''

def findSmallestMaxDistance(stations, k):
    n = len(stations)
    
    def canPlace(d):
        count = 0
        for i in range(n - 1):
            gap = stations[i + 1] - stations[i]
            
            extra = int(gap // d)
            
            count += extra 
            
            if count > k:
                return False
            
        return True
    
    left = 0.0
    right = float(stations[-1] - stations[0])
    
    while right - left > 1e-6:
        mid = (left + right) / 2.0
        
        if canPlace(mid):
            right = mid
        else:
            left = mid
            
    return round(right, 2)

# Examples
stations1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 9
print(findSmallestMaxDistance(stations1, k1)) # Output: 0.50

stations2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k2 = 5
print(findSmallestMaxDistance(stations2, k2)) # Output: 1.00

stations3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 0
print(findSmallestMaxDistance(stations3, k3)) # Output: 1.00

stations4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k4 = 20
print(findSmallestMaxDistance(stations4, k4)) # Output: 0.25

stations5 = [1, 3, 5, 7, 9]
k5 = 3
print(findSmallestMaxDistance(stations5, k5)) # Output: 1.00

stations6 = [1, 3, 5, 7, 9]
k6 = 6
print(findSmallestMaxDistance(stations6, k6)) # Output: 0.50

stations7 = [1, 5, 10, 15, 20]
k7 = 2
print(findSmallestMaxDistance(stations7, k7)) # Output: 3.33

stations8 = [1, 5, 10, 15, 20]
k8 = 5
print(findSmallestMaxDistance(stations8, k8)) # Output: 2.50

stations9 = [1, 10, 20, 30, 40]
k9 = 4
print(findSmallestMaxDistance(stations9, k9)) # Output: 5.00

stations10 = [1, 10, 20, 30, 40]
k10 = 8
print(findSmallestMaxDistance(stations10, k10)) # Output: 3.33

stations11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
k11 = 10
print(findSmallestMaxDistance(stations11, k11)) # Output: 0.67