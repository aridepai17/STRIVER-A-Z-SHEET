# MINIMUM NUMBER OF DAYS TO MAKE M BOUQUETS

'''
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
'''

def minDays(bloomDay, m, k):
    n = len(bloomDay)
    
    if m * k > n:
        return -1
    
    ans = -1
    left = min(bloomDay)
    right = max(bloomDay)
    
    while left <= right:
        mid = (left + right) // 2
        
        adjacentCount = 0
        bouquetCount = 0
        
        for bloom in bloomDay:
            if bloom <= mid:
                adjacentCount += 1
                if adjacentCount == k:
                    bouquetCount += 1
                    adjacentCount = 0
            else:
                adjacentCount = 0

        if bouquetCount >= m:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans

# Examples
bloomDay1, m1, k1 = [1,10,3,10,2], 3, 1
print(minDays(bloomDay1, m1, k1)) # Output: 3

bloomDay2, m2, k2 = [1,10,3,10,2], 3, 2
print(minDays(bloomDay2, m2, k2)) # Output: -1

bloomDay3, m3, k3 = [7,7,7,7,12,7,7], 2, 3
print(minDays(bloomDay3, m3, k3)) # Output: 12

bloomDay4, m4, k4 = [1,10,3,10,2], 3, 2
print(minDays(bloomDay4, m4, k4)) # Output: -1

bloomDay5, m5, k5 = [1,2,3,4,5], 2, 2
print(minDays(bloomDay5, m5, k5)) # Output: 4

bloomDay6, m6, k6 = [1,2,3,4,5], 1, 3
print(minDays(bloomDay6, m6, k6)) # Output: 3

bloomDay7, m7, k7 = [1,1,1,1,1], 2, 2
print(minDays(bloomDay7, m7, k7)) # Output: 1

bloomDay8, m8, k8 = [5,5,5,5,5], 2, 3
print(minDays(bloomDay8, m8, k8)) # Output: 5

bloomDay9, m9, k9 = [1,2,3,4,5,6], 3, 2
print(minDays(bloomDay9, m9, k9)) # Output: 5

bloomDay10, m10, k10 = [1,2,3,4,5,6], 2, 3
print(minDays(bloomDay10, m10, k10)) # Output: 5

bloomDay11, m11, k11 = [1,2,3,4,5,6], 1, 6
print(minDays(bloomDay11, m11, k11)) # Output: 6