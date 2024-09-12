# You are given two positive integers a and b. Print the LCM of these two numbers.

a,b = map(int,input().split())
min,i,hcf,lcm = 0,1,0,0
if a>b:
    min = b
else:
    min = a
while i<=min:
    if a%i==0:
        if b%i==0:
            hcf = i
    i += 1
lcm = (a*b)//hcf
print(lcm)

