# You are given an integer array. Find the index of the minimum element of the array. If there are multiple occurrences of the minimum number, print the index of the first occurrence of the minimum number. 
# Note: The index will be calculated from 1.
# Sample Input: 
# 10 5 6 3 4 3 5 6
# Sample Output: 
# 4

arr = [10 ,5 ,6 ,8 ,4 ,3 ,5 ,6]
i,min,minindex = 0,arr[0],0
while i<len(arr):
    if min>arr[i]:
        if arr[i] != min:
            min = arr[i]
            minindex = i
    i += 1   
print(minindex+1)

