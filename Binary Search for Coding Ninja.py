# Array submitted on Coding Ninja website
# This binary search takes in input from the user on the array and target

def binary_search(list, target):
    
    upperbound, lowerbound, found = len(list) - 1, 0, False
    
    while lowerbound <= upperbound:
        index = (upperbound + lowerbound) // 2

        if target == list[index]:
            found = True
            break
        elif target > list[index]:
            lowerbound = index + 1
        else:
            upperbound = index - 1

    if found:
        print(index)
    else:
        print(-1)

#Input
N = int(input())
list = list(map(int, input().split()))
target = int(input())

#Output
binary_search(list, target)