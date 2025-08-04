# BEST TIME TO BUY AND SELL STOCK 

'''
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. Determine the maximum profit achievable by buying and selling the stock at most once. 
The stock should be purchased before selling it, and both actions cannot occur on the same day.
'''

def stockBuyandSell(nums):
    maxPrice = float('-inf')
    minPrice = float('inf')
    
    for price in nums:
        minPrice = min(minPrice, price)
        maxPrice = max(maxPrice, price - minPrice)
        
    return maxPrice

# Examples
nums1 = [10, 7, 5, 8, 11, 9]
print(stockBuyandSell(nums1)) # Output: 6

nums2 = [10, 22, 5, 75, 65, 80]
print(stockBuyandSell(nums2)) # Output: 87

nums3 = [90, 80, 70, 60, 50, 40]
print(stockBuyandSell(nums3)) # Output: 0

# New examples
nums4 = [1, 2, 3, 4, 5]
print(stockBuyandSell(nums4)) # Output: 4

nums5 = [5, 4, 3, 2, 1]
print(stockBuyandSell(nums5)) # Output: 0

nums6 = [3, 2, 6, 5, 0, 3]
print(stockBuyandSell(nums6)) # Output: 4

nums7 = [7, 1, 5, 3, 6, 4]
print(stockBuyandSell(nums7)) # Output: 5

nums8 = [1, 4, 3, 2, 5]
print(stockBuyandSell(nums8)) # Output: 4

nums9 = [10, 20, 30, 40, 50]
print(stockBuyandSell(nums9)) # Output: 40

nums10 = [50, 40, 30, 20, 10]
print(stockBuyandSell(nums10)) # Output: 0

nums11 = [1, 3, 2, 8, 4, 9]
print(stockBuyandSell(nums11)) # Output: 8

nums12 = [2, 1, 2, 1, 2]
print(stockBuyandSell(nums12)) # Output: 1
        