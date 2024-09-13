# You are given an array of integers. Check if the given array is a Palindrome. If it is a Palindrome array, print yes, else print no.
# Note: A Palindrome Array is when the reverse of the array is the same as the original array.
# Sample Input 1:
# 11 1 13 21 3 7
# Sample Output 1:
# No
# Sample Input 2:
# 17 1 13 1 17
# Sample Output 2:
# Yes


arr = [17 ,1 ,13 ,12 ,1 ,17]
i,length,count = 0, len(arr)-1,0
while i<=length//2:
    if arr[i] == arr[length-i]:
        count += 1
    i += 1
if count-1 == length//2:
    print("Yes")
else:
    print("No")

