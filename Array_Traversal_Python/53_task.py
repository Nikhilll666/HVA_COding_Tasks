# You are given an array of integers. Check if the array is in Ascending Order. If yes, print "Yes", else print "No.
# Sample Input 1:
# 3 5 10 13 16 12 14
# Sample Output 1:
# No
# Explanation 1: The given array is not in ascending order.
# Sample Input 2:
# 3 5 10 13 16 25 33
# Sample Output 2:
# Yes


arr = [3 ,5 ,10 ,13 ,16 ,25 ,33]
i, count = 0, 0
while i<len(arr)-1:
    if arr[i]>arr[i+1]:
        count += 1
        break 
    i += 1

if count>0:
    print("No")
else:
    print("Yes")
