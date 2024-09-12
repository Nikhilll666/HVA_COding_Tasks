# You are given an integer array. You are also given a number. Print the number of times the number appears in the array.
# Sample Input:
# 4 7 9 10 7 14 12 4 7 27
# 7
# Sample Output: 
# 3

arr = [4 ,7 ,9 ,10 ,7 ,14 ,12 ,4 ,7 ,27]
n = int(input())
i,count = 0,0
while i<len(arr):
    if arr[i]==n:
        count += 1
    i += 1
print(count)
