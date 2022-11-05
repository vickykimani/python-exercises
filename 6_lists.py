# declare and initialize a list
fruits = ["orange", "peach", "banana", "mango", "plum"]
print(fruits)

# loop through entire list of fruits
for fruit in fruits:
    print(fruit)

# retrieve list items
print(f"the fruit at position 1: {fruits[0]}")
print(f"the fruit at the end of the list: {fruits[-1]}")

# check length of the list
print(f"the fruit basket currently has {len(fruits)} fruits")

# add sth to the list
fruits.append("lemon")
print(fruits)

# check the length of the list
print(f"the fruit basket currently has {len(fruits)} fruits")

# add a list item to a specific position in the list
fruits.insert(2, "apple")
print(fruits)

# remove specific item from the list
fruits.remove("lemon")
print(fruits)

# remove item from a specified index on the list
fruits.pop(0)
print(fruits)

# remove item from the end of list
fruits.pop()
print(fruits)
