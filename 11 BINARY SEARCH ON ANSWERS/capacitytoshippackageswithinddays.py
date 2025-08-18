# CAPACITY TO SHIP PACKAGES WITHIN D DAYS

'''
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. 
Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
'''

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)
    
    while left <= right:
        mid = (left + right) // 2
        
        currentWeight = 0
        daysNeeded = 1
        
        for weight in weights:
            if currentWeight + weight > mid:
                daysNeeded += 1
                currentWeight = weight
            else:
                currentWeight += weight
        
        if daysNeeded <= days:
            right = mid - 1
        else:
            left = mid + 1
            
    return left


# Examples
weights1 = [1,2,3,4,5,6,7,8,9,10]
days1 = 5
print(shipWithinDays(weights1, days1))  # Output: 15

# Additional examples
weights2 = [3,2,2,4,1,4]
days2 = 3
print(shipWithinDays(weights2, days2))  # Output: 6

weights3 = [1,2,3,1,1]
days3 = 4
print(shipWithinDays(weights3, days3))  # Output: 3

weights4 = [10]
days4 = 1
print(shipWithinDays(weights4, days4))  # Output: 10

weights5 = [10]
days5 = 2
print(shipWithinDays(weights5, days5))  # Output: 10

weights6 = [5,5,5,5]
days6 = 2
print(shipWithinDays(weights6, days6))  # Output: 10

weights7 = [5,5,5,5]
days7 = 4
print(shipWithinDays(weights7, days7))  # Output: 5

weights8 = [7,2,5,10,8]
days8 = 2
print(shipWithinDays(weights8, days8))  # Output: 18

weights9 = [1,1,1,1,1,1,1,1,1,1]
days9 = 5
print(shipWithinDays(weights9, days9))  # Output: 2

weights10 = [9,8,10]
days10 = 3
print(shipWithinDays(weights10, days10))  # Output: 10

weights11 = [9,8,10]
days11 = 1
print(shipWithinDays(weights11, days11))  # Output: 27

