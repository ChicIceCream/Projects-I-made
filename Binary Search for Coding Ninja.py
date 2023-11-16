# Array submitted on Coding Ninja website
# This binary search takes in input from the user on the array and target


N = int(input())
arr = list(map(int, input().split()))
target = int(input())


upperbound, lowerbound, found = len(arr) - 1, 0, False

while lowerbound <= upperbound:
    index = (upperbound + lowerbound) // 2

    if target == arr[index]:
        found = True
        break
    elif target > arr[index]:
        lowerbound = index + 1
    else:
        upperbound = index - 1

if found:
    print(index)
else:
    print(-1)
