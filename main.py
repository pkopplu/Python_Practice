# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
def bmi(weight, height):
    BMI = weight/(height*height)
    return BMI
def a_to_b(name):
    name_replaced = name.replace('a','b')
    return name_replaced

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     weight_kg = float(input())
#     height_m=float(input())
#     body_mass_index = (bmi(weight_kg,height_m))
#     print(f"The BMI is {body_mass_index}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
