# You are given an integer n. Print first n terms of the series 2, 5, 8, 11, 14…

n = int(input())
i,a = 0,2
while i<n:
    print(a, end =" ")
    i += 1
    a += 3
print('\n')