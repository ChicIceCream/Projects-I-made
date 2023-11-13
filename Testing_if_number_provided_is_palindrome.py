list1 = input("Enter your number : ")
# print(list1)

reversed_list = list1[::-1]
# print(reversed_list)

if list1 == reversed_list:
    print("Yes this is a palindrome number")
else:
    print("No this is not a palindrome number")