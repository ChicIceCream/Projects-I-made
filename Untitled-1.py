def isPerfectSquare(num):
    global result
    result = False
    left = 1
    right = num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > num:
            right = mid - 1
        elif mid * mid < num:
            right = mid + 1
        else:
            result = True
    return False

num = 4
isPerfectSquare(num)
if result is True:
    print("Good")
else:
    print("Failed")