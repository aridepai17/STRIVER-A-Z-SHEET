# KOKO EATING BANANAS

'''
Koko loves to eat bananas. 
There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
'''

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    
    while left <= right:
        mid = (left + right) // 2
        
        hours = 0
        
        for pile in piles:
            hours += (pile + mid - 1) // mid
            
        if hours <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left

# Examples
piles1, h1 = [3,6,7,11], 8
print(minEatingSpeed(piles1, h1)) # Output: 4

piles2, h2 = [30,11,23,4,20], 5
print(minEatingSpeed(piles2, h2)) # Output: 30

piles3, h3 = [30,11,23,4,20], 6
print(minEatingSpeed(piles3, h3)) # Output: 23

piles4, h4 = [1,1,1,1], 4
print(minEatingSpeed(piles4, h4)) # Output: 1

piles5, h5 = [1,1,1,1], 2
print(minEatingSpeed(piles5, h5)) # Output: 2

piles6, h6 = [10], 1
print(minEatingSpeed(piles6, h6)) # Output: 10

piles7, h7 = [10], 10
print(minEatingSpeed(piles7, h7)) # Output: 1

piles8, h8 = [5,5,5,5], 4
print(minEatingSpeed(piles8, h8)) # Output: 5

piles9, h9 = [5,5,5,5], 5
print(minEatingSpeed(piles9, h9)) # Output: 4

piles10, h10 = [100,50,25], 3
print(minEatingSpeed(piles10, h10)) # Output: 100

piles11, h11 = [100,50,25], 4
print(minEatingSpeed(piles11, h11)) # Output: 75