#Fibonacci series 
# input 
num_1, num_2 = 1, 1
print(num_1)
print(num_2)
# loops start from now
for i in range(2, 9):
    num_3 = num_1 + num_2
    print(num_3)
    num_1, num_2 = num_2, num_3

# To get the expected output
# we can keep adding the previous two numbers until we reach the desired number of terms. 
# For example :
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34
# this is how we will get the expected output 
#----------------------------------------------------------------------
# Output:
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
#----------------------------------------------------------------------
