# You are given an integer array. Take another number as input and search if the number is present in the given array. If the number is present, print "Yes", else print "No".
# Sample Input 1:
# 11 1 13 21 3 7
# 3
# Sample Output 1:
# Yes
# Sample Input 2:
# 11 1 13 21 3 7
# 5
# Sample Output 2:
# No


arr = [11 ,1 ,13 ,21 ,3 ,7]
n ,i,count = int(input()) ,0,0
while i<len(arr):
    if arr[i]==n:
        count += 1
        break
    i += 1
if count>0:
    print("Yes")
else:
    print("No")
