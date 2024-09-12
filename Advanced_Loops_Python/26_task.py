# Write a program that takes a number n as input and prints the reverse of the given number.

n = int(input())
reverse = 0
while n>0:
    x = n%10
    reverse = reverse*10 +x
    n = n//10
print(reverse)