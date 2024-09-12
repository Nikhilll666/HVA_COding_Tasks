# You are given an integer n. Print the first n square numbers.

n = int(input())
i,count = 1,0
while count<n:
    print(i**2, end= " ")
    i,count = i+1,count+1
print('\n')
