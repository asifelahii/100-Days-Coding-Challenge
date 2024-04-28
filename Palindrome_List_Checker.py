# Write a program to check if a list is a palindrome or not.
list = [] #initializing an empty list

# Taking input from user and apending to list.
list.append(input("Enter element 01:"))
list.append(input("Enter element 02:"))
list.append(input("Enter element 03:"))
list.append(input("Enter element 04:"))
list.append(input("Enter element 05:"))

print(list) # Prints original list

new_list = list.copy() # make a copy of the original list and assigns it to new_list
new_list.reverse() # reverse new_list [reversing the original list indirectly]

# Checking if the original list is equal to the reversed list.
if list == new_list:
        print("The list is a palindrome.")
else: print("Not palindrome.")