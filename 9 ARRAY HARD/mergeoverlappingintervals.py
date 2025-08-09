# MERGE OVERLAPPING INTERVALS

'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

def mergeOverlaps(intervals):
    intervals.sort()
    merged = []
    
    for current in intervals:
        if not merged or current[0] > merged[-1][1]:
            merged.append(current)
        else:
            merged[-1][1] = max(current[1], merged[-1][1])
            
    return merged

# Examples
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(mergeOverlaps(intervals1)) # Output: [[1,6],[8,10],[15,18]]

# Additional examples
intervals2 = [[1,4],[4,5]]
print(mergeOverlaps(intervals2)) # Output: [[1,5]]

intervals3 = [[1,4],[2,3]]
print(mergeOverlaps(intervals3)) # Output: [[1,4]]

intervals4 = [[1,2],[3,4],[5,6]]
print(mergeOverlaps(intervals4)) # Output: [[1,2],[3,4],[5,6]]

intervals5 = [[1,10],[2,6],[8,10],[15,18]]
print(mergeOverlaps(intervals5)) # Output: [[1,10],[15,18]]

intervals6 = [[1,5],[2,3],[4,6],[7,8]]
print(mergeOverlaps(intervals6)) # Output: [[1,6],[7,8]]

intervals7 = [[1,2],[2,3],[3,4],[4,5]]
print(mergeOverlaps(intervals7)) # Output: [[1,5]]

intervals8 = [[1,3],[5,7],[2,4],[6,8]]
print(mergeOverlaps(intervals8)) # Output: [[1,4],[5,8]]

intervals9 = [[1,2],[3,5],[4,6],[7,8]]
print(mergeOverlaps(intervals9)) # Output: [[1,2],[3,6],[7,8]]

intervals10 = [[1,2],[2,3],[3,4],[4,5],[5,6]]
print(mergeOverlaps(intervals10)) # Output: [[1,6]]