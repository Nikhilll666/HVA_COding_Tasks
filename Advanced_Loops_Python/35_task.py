# Print the following pattern based on the given input.
# Sample Input: 
# 6
# Sample Output: 
#      *
#     **
#    ***
#   ****
#  *****
# ******

n = int(input())
i = 1
while i<=n:
    print((n-i)*(" ") + ("*")*i)
    i += 1
