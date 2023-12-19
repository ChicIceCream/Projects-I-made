def create_new_array(lst):
    new_array = [elem + index for index, elem in enumerate(lst)]
    return new_array

# Example usage:
original_list = [2, 3, 1, 1, 4]
new_list = create_new_array(original_list)

print("Original List:", original_list)
print("New List:", new_list)
