# ALLOCATE MINIMUM PAGES

'''
Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. 
You also have an integer k representing the number of students. 
The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
The objective is to minimize the maximum number of pages assigned to any student. 
In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: If it is not possible to allocate books to all students, return -1.
'''

def findPages(arr, k):
    n = len(arr)
    
    if k > n:
        return -1
    
    def findStudents(pages, arr):
        students = 1
        studentsPages = 0
        
        for i in range(n):
            if studentsPages + arr[i] <= pages:
                studentsPages += arr[i]
            else:
                students += 1
                studentsPages = arr[i]
                
        return students
    
    left = max(arr)
    right = sum(arr)
    
    while left <= right:
        mid = (left + right) // 2
    
    noOfStudents = findStudents(mid, arr)
    
    if noOfStudents > k:
        left = mid + 1
    else:
        right = mid - 1
        
    return left

# Examples
arr1 = [12, 34, 67, 90], k1 = 2
print(findPages(arr1, k1)) # Output: 113

arr2 = [10, 20, 30, 40], k2 = 2
print(findPages(arr2, k2)) # Output: 60

arr3 = [15, 17, 20], k3 = 1
print(findPages(arr3, k3)) # Output: 52

arr4 = [5, 10, 15, 20], k4 = 4
print(findPages(arr4, k4)) # Output: 20

arr5 = [10, 20, 30], k5 = 5
print(findPages(arr5, k5)) # Output: -1

arr6 = [100, 200, 300, 400, 500], k6 = 3
print(findPages(arr6, k6)) # Output: 700

arr7 = [25, 25, 25, 25, 25], k7 = 2
print(findPages(arr7, k7)) # Output: 75

arr8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k8 = 3
print(findPages(arr8, k8)) # Output: 21

arr9 = [50, 60, 70, 80], k9 = 4
print(findPages(arr9, k9)) # Output: 80

arr10 = [2, 8, 15, 10, 5, 12, 7, 18, 3, 9, 11, 4, 6, 13, 16], k10 = 4
print(findPages(arr10, k10)) # Output: 45