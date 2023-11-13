def find_max(array):
    if not array:
        return None  # or raise an exception, depending on your requirements
    
    max_element = array[0]
    for element in array[1:]:
        if element > max_element:
            max_element = element

    return max_element

array = [12, 45, 34, 6, 2]
result = find_max(array)
print(f"The maximum element in the array is {result}")
