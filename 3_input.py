# input in python
# python uses the function input() to capture and store information from the user.

print("User Profile Application")
first_name = input("First Name: ")
last_name = input("Last Name: ")
occupation = input("Your Job: ")

print("Your first name is: " + first_name)
print("Your last name is: " + last_name)
print("Your job is: " + occupation)


# another way of outputting information in python is through formatted strings
print(f"Your first name is {first_name} and your job is {occupation}")

# handling non-string input
age = input("Please enter your age: ")
print(f"In two years your age will be {age+2} ")
