# You are given an array of integers. Print the first element of the array that is a perfect square. If there are no perfect squares, print No.
# Sample Input 1:
# 3 6 7 4 6 9 1 23
# Sample Output 1:
# 4
# Explanation 1: In the given array, the first perfect square to appear is 4.
# Sample Input 2:
# 10 8 14 11 6 15
# Sample Output 2:
# No

arr = [3 ,6 ,7 ,4 ,6 ,9 ,1 ,23]
i, count = 0, 0
while i<len(arr):
    half = arr[i]/2
    if half**2 == arr[i]:
        count += 1
        print(arr[i])
        break
    i += 1
if count == 0:
    print("No")

