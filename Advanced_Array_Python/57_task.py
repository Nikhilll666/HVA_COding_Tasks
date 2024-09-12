# You are given an array of integers. Create a new array with elements in reverse order. Print the new array.
# Sample Input:
# 11 1 13 21 3 7
# Sample Output:
# 7 3 21 13 1 11


arr = [11 ,1 ,13 ,21 ,3 ,7]
i, length = 0, len(arr)-1

while i<=length:
    print(arr[length-i], end = " ")
    i += 1
print('\n')