# You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…

n = int(input())
i = 1
ans = 3*i
while i<=n:
    print(ans, end =" ")
    i += 1
    ans *= 2
print()
