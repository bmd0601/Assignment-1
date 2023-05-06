# The datatype which i used to get the expected output is list
# input
length_1 = int(input("Please enter the total number of elements: "))
lst = []
even_list = []
odd_list = []

for i in range(length_1):
    element = int(input("Please enter an element: "))
    lst.append(element)

for x in lst:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

print(f"Number of even numbers: {len(even_list)}")
print(f"Number of odd numbers: {len(odd_list)}")

# please enter all the elements individually to get the expected output
# for example:
# Please enter the total number of elements: 9
# Please enter an element: 1
# Please enter an element: 2
# Please enter an element: 3
# Please enter an element: 4
# Please enter an element: 5
# Please enter an element: 6
# Please enter an element: 7
# Please enter an element: 8
# Please enter an element: 9
#----------------------------------------------------------------------
# Output:
# Number of even numbers: 4
# Number of odd numbers: 5
#----------------------------------------------------------------------
