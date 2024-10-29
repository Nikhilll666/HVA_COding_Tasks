# You are given an integer n. Print the first n prime numbers.
# Sample Input: 
# 7
# Sample Output: 
# 2 3 5 7 11 13 17

n = int(input())
i,gretcount = 1,0
while gretcount<n:
    j,count = 1,0
    while j<=i/2:
        if i%j == 0:
            count += 1
        j += 1
    if count == 1:
        gretcount += 1
        print(i,end = " ")
    i += 1
print()
