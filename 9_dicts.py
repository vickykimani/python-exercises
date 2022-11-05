# python uses dictionaries to store key-value pairs
# from python 3.7 upwards, dicts are ordered.
# dicts don't allow duplicate values.
# dicts are changeable
# dicts are implemented using curly braces.

# declaring a dictionary:
my_phone = {
    "Brand": "Samsung",
    "Make": "Galaxy",
    "Model": "S22",
    "YoM": "2022",
    "Origin": "South Korea"
}

print(my_phone)

print(f"my phone is a {my_phone['Brand']}")
print(f"my phone is a {my_phone['Brand']} {my_phone['Model']}")

my_phones = {
    "phone_one": {
        "Brand": "Samsung",
        "Make": "Galaxy",
        "Model": "S22",
        "YoM": "2022",
        "Origin": "South Korea"
    },
    "phone_two": {
        "Brand": "Apple",
        "Make": "iPhone",
        "Version": "13",
        "YoM": "2021",
        "Origin": "USA"
    },
    "phone_three": {
        "Brand": "Google",
        "Make": "Pixel",
        "Version": "6 Pro",
        "YoM": "2021",
        "Origin": "USA"
    }
}

print(my_phones["phone_two"])

print("printing all the phones in the dictionary...")
for phone in my_phones:
    print(my_phones[phone])
