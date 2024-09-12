# You are given an integer array. Print the length of the longest subarray with increasing numbers.
# A subarray is defined as a contiguous portion of an array.
# Try not to use nested loop.
# Sample Input: 
# 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
# Sample Output: 
# 4

arr = [5 ,4 ,4 ,7 ,6 ,3 ,2 ,4 ,6 ,8 ,6 ,3 ,6 ,8 ,5]
i,maxcount = 0, 0
n = len(arr)
while i<n:
    j = 0
    while j<n-i:
        k = i
        count = 0
        while k<=i+j-1:
            if arr[k]<arr[k+1]:
                count += 1
            else:
                break
            k += 1
        if count>maxcount:
            maxcount = count
        j += 1
    i += 1
print(maxcount+1)



