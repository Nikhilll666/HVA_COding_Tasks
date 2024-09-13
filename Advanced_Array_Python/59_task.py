# You are given an array of integers. Find the element that appears the maximum number of times in an array. If multiple elements appear maximum number of times, you can print any.
# Sample Input:
# 5 4 7 11 8 4 6 11 9
# Sample Output:
# 4

arr = [5 ,4 ,7 ,11 ,8 ,4 ,6 ,11 ,9]
i,maxcount,val = 0,0,0
while i<len(arr):
    j,count = i+1,0
    while j<len(arr)-1:
        if arr[i] == arr[j]:
            count += 1
        j += 1
    if count>maxcount:
        maxcount = count
        val = arr[i]
    i += 1
print(val)
