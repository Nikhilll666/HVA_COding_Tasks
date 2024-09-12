# You are given an integer array. Count all the numbers present in the array till you encounter a negative number and print the count. If no negative number is present, count till the end.
# Sample Input: 
# 10 5 6 3 -1 4 -3 5 6
# Sample Output: 
# 4

arr = [10 ,5 ,6 ,3 ,-1 ,4 ,-3 ,5 ,6]
i ,count= 0,0
while i<len(arr):
    if arr[i]>0:
        count += 1
    else:
        print(count)
        break
    i += 1
    