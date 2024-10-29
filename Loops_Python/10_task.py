# You are given an integer n. Print all the even numbers less than equal to n.

n = int(input())
i = 2
while i<=n:
    print(i, end=" ")
    i += 2
print()