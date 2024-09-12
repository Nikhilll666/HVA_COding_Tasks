# You are given an integer n. Print yes, if it is a prime number. Print no, if it is not a prime number.

n = int(input())
i,count = 1,0
while i<=n/2:
    if n%i==0:
        count += 1
    i += 1
if count == 1:
    print("Yes")
else:
    print("No")
