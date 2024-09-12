# Write a program that takes three numbers as input and prints the numbers in ascending order.
# This program doesn't use an array.

a,b,c = map(int,input().split())
if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)
elif b>c and b>a:
    if a>c:
        print(c,a,b)
    else:
        print(a,c,b)
elif a>b:
    print(b,a,c)
else:
    print(a,b,c)

