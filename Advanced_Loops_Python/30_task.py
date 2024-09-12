# Write a program that takes a Decimal Number D as input and prints the Binary equivalent of the given input.

n = int(input())
i, binary = 0, 0
while n>0:
    r = n%2
    binary = binary + r*(10**i)
    n = n//2
    i += 1
print(binary)


