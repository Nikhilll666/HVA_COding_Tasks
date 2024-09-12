# Write a program that takes a Binary Number B as input and prints the Decimal equivalent of the given input.

n = int(input())
i,decimal = 0,0
while n>0:
    x = n%10
    decimal += x*(2**i)
    i += 1
    n = n//10
print(decimal)
