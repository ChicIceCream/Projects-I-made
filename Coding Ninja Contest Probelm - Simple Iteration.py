'''
You are given three integers, 'X', 'Y', and 'Z'.
Your task is to discover and return all integers from the range of '1' to 'Z'. The integers should be such that when divided by 'X', they yield a remainder of Y°.
Note The sequence of these returned integers can be in any order
'''

#Start of function
def iterateTillZ(list, x, y, z):
    for index in range(len(list[0:z])):
        if list[index] % x == y:
            print(list[index])

list = [1,2,3,4,5,6,7,8,9,10]

# Can be optimsed, but sometimes its better to make it simple
x = int(input())
y = int(input())
z = int(input())
iterateTillZ(list, x, y, z) # prints the function