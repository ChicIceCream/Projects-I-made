def rotated_finder(array):
    # check if the number at index is bigger than the number after it
    for index in range(len((array))):
        if array[index] < array[index + 1]:
            print("This is the number when it was rotated")
            print(index)
            break

#! DOESNT WORK WHEN LIST IS IN ORDER
#! FIX THIS
list = [2,1,0,3,4,5,6]
rotated_finder(list)