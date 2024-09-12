# You are given two positive integers a and b. Print the GCD or HCF of these two numbers.

a,b = map(int,input().split())
min,i,hcf = 0,1,0
if a>b:
    min = b
else:
    min = a
while i<=min:
    if a%i==0:
        if b%i==0:
            hcf = i
    i += 1
print(hcf)
