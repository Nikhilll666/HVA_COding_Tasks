# You are given an integer n. Print the sum of the first n Natural Numbers.

n = int(input())
i,sum = 1,0
while i<=n:
    sum += i
    i += 1
print(sum)
