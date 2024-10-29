# You are given an integer n. Print all the square numbers less than equal to n.

n = int(input())
i = 1
while i**2 <= n:
    print(i**2, end=" ")
    i += 1
print()
