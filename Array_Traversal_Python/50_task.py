# You are given an integer array. Add all the numbers present in the array till you encounter a 0 and print the sum. If no 0 is present, add till the end.
# Sample Input: 
# 10 5 6 3 0 4 3 5 6
# Sample Output: 
# 24

arr = [10 ,5 ,6 ,3 ,0 ,4 ,3 ,5 ,6]
i ,sum= 0, 0
while i<len(arr):
    if arr[i]!=0:
        sum += arr[i]
    else:
        print(sum)
        break
    i += 1
  