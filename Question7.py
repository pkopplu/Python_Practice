# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# exmaple
# first name : MOhit
# last name : sharma
# age 32
#
# Display : my name is Mohit Sharma and I am 32 years old.
#
# note that first letter of first name and last name both should be in capital letters and rest in small.

def print_info(first, last, age):
    first = first[0].upper() + first[1:].lower()
    last =last[0].upper() +last[1:].lower()
    print(f"my name is {first} {last} and I am {age} years old.")

print("Enter first name:")
first = input()
print("Enter last name:")
last = input()
print("Enter age:")
age = input()
print_info(first, last, age)