# Write a program that takes a number n as input and prints the number of digits the number has.

n = int(input())
count = 0
while n>0:
    count += 1
    n = n//10
print(count)
