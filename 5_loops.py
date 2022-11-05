# python implements loops using the 'for' statement
# accompanied by additional logic
# my_fruits = ["mango", "orange", "peach", "apple"]
# for fruit in my_fruits:
#     print(fruit)
# print(f"The list {my_fruits} has {len(my_fruits)} items.")

# my_name = "Jonathan"
# for i in my_name:
#     print(i)

# dynamic looping using for ...in ... range
# n = 1
# starting_value = 1
# for i in range(starting_value, 20+n):
#     print(i)

# dynamic looping using for ...in ... range (with a 'step')
# initial_value = 2
# step = 4
# max_value = 21
# for i in range(initial_value, max_value, step):
#     print(i)

# while loop in python
count = 0
while (count <= 10):
    print(f"count is currently: {count}")
    if (count % 2 == 0):
        print(f"{count} is even.")
    else:
        print(f"{count} is odd.")
    count += 1
print("end of loop.")
