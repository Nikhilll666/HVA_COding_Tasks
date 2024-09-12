# You are given an integer n. Print yes, if it is an Armstrong Number. Print no, if it is not an Armstrong Number.

n = int(input())
x, count, armstrong = n, 0, 0
while x>0:
    count += 1
    x = x//10
x = n
while x>0:
    rem = x%10
    armstrong += rem**count
    x = x//10
if armstrong == n:
    print("Yes")
else:
    print("No")

