# Print the following pattern based on the given input.
# Sample Input: 
# 5
# Sample Output: 
#     *
#    ***
#   *****
#  *******
# *********

n = int(input())
i,star = 1,1
while i<=n:
    print(" "*(n-i) + ("*")*star)
    i += 1
    star += 2
    