# Write a program that takes a number n as input and prints the first n terms of the Fibonacci Series.
# The Fibonacci Series is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

n = int(input())
a,b,i = 0,1,0
while i<n:
    print(a,end = " ")
    a,b = b,a+b
    i += 1
print('\n')
