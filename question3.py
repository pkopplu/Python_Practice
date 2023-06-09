# 3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest (float) and print the expected total amount  after  2 years.
#
# example : principle : 100 , interest percent 10  then amount after 2 years will be : 100*1.1*1.1 = 121
def total(amount, interest):
    return amount*(1+interest)*(1+interest)
amount =int(input())
interest =float(input())
print(total(amount,interest))