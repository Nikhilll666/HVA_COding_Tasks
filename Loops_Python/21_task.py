# You are given an integer n. Print the sum of the first n terms of the series 3, 5, 7, 9, 11….

n = int(input())
i,a,sum = 0,3,0
while i<n:
    sum += a
    i += 1
    a += 2
print(sum)

