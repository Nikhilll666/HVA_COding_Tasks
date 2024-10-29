# Write a program that takes a number n as input and prints all the factors of the number

n = int(input())
i = 1
while i<=n:
    if n%i==0:
        print(i, end =" ")
    i += 1
print()
