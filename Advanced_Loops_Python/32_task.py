# You are given an integer n. Print yes, if it is a Perfect Number. Print no, if it is not a Perfect Number.

n = int(input())
i,sum = 1,0
while i<=n/2:
    if n%i==0:
        sum += i
    i += 1
if sum == n:
    print("Yes")
else:
    print("No")
