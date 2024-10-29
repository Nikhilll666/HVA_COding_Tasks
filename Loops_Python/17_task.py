# You are given an integer n. Print first n terms of the series 3, 5, 7, 9, 11…

n = int(input())
i,a = 0,3
while i<n:
    print(a, end =" ")
    i += 1
    a += 2
print()
