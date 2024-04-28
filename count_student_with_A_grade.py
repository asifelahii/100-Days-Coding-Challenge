"""Write a programme to count the number of students with 'A' grade"""
list = [] # creating an empty list

# Taking grades as input from user & storing them in the list.
list.append(input("Enter students grade: "))
list.append(input("Enter students grade: "))
list.append(input("Enter students grade: "))
list.append(input("Enter students grade: "))
list.append(input("Enter students grade: "))

print(list) # prints original list
print(list.count('A')) # prints the number of students with grade 'A'