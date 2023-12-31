# This uses a function so it is easier to call it directly

def find_max(array):
    if not array:
        return None # this is to make sure that the array is not empty
    
    max_element = array()
    for element in array[1:]: # using [1:] means to go from the first index to the end as we have specified the first index as the max_elemnt
        if element > max_element:
            max_element = element # will switch the element that is bigger than the max_element to the max_element

    return max_element

array = [2,5,24,22,4,,6] # example of an array i used
result = find_max(array)
if result == None:
    print("There is no max element as the array is empty")
else: 
    print(f"The maximum element in the array is {result}")