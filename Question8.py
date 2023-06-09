# 8-take 3 inputs from user : first name , last name and company name.
# create the email alias for the user and display it.
# Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example
# first name : MOhit
# last name : sharma
# company : infosys
#
# Display : morma@infosys.com
#
# note full email id should -be in lower case

def alias(first, last, company):
    first = first[0:2].lower()
    last = last[-3:].lower()
    company = f'@{company}.com'
    print(f'{first}{last}{company}')

print("enter first name:")
first =input()
print("enter last name")
last =input()
print("enter company name")
company=input()
alias(first,last,company)

