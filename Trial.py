def isPerfectSquare(num):
    array = list(range(1**2, (num **2) + 1)
    upper_bound = len(array) - 1
    lower_bound = 0 
    print(upper_bound, lower_bound, array)
    for index in enumerate(array):
        if lower_bound <= upper_bound:
            index = (upper_bound + lower_bound) // 2

            if num == array[index]:
                return True
                return index
                print(array[index])
                elif num >= array[index]:
                    lower_bound = index + 1
                else:
                    upper_bound = index - 1
            
            return -1

num = int(input("Enter your number : "))
isPerfectSquare(num)