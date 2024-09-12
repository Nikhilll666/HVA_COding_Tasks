# You are given an integer n. Print the first n even numbers.

n = int(input())
i,count = 2,0
while count<n:
    print(i, end= " ")
    i,count = i+2,count+1
print('\n')

    