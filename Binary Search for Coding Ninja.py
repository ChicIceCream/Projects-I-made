# Array submitted on Coding Ninja website
# This binary search takes in input from the user on the array and target

def binary_search(arr, target):
    
    upperbound, lowerbound = len(arr) - 1, 0
    
    while lowerbound <= upperbound:
        index = (upperbound + lowerbound) // 2

        if target == arr[index]:
            return index
        elif target > arr[index]:
            lowerbound = index + 1
        else:
            upperbound = index - 1

    return -1
#Input
N = int(input())
list = list(map(int, input().split()))
target = int(input())

#Output
print(binary_search(list, target))