# You are given an array of integers and another integer K. Print the first element of the array that is greater than K. If there are no elements greater than K, print No.
# Sample Input 1:
# 3 5 10 25 16 12 14
# 11
# Sample Output 1:
# 25
# Explanation 1: In the given array, the first element greater than 11 is 25.
# Sample Input 2:
# 3 5 10 13 16 12 14
# 19
# Sample Output 2:
# No

arr = [3 ,5 ,10 ,25 ,16 ,12 ,14]
n, i, count = int(input()), 0, 0
while i<len(arr):
    if arr[i]>n:
        count += 1
        print(arr[i])
        break
    i += 1
if count == 0:
    print("No")
