# You are given an integer array. Multiply all the numbers present in the array and print the final product.
# Sample Input: 
# 3 2 5 1 4
# Sample Output: 
# 120
# Explanation: 3*2*5*1*4 = 120

arr = [3 ,2 ,5 ,1 ,4]
i,multiple = 0,1
while i<len(arr):
    multiple *= arr[i]
    i += 1
print(multiple)
