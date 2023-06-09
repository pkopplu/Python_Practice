# 4- write a program which takes city name from user input. irrespective of in which case user enters the city name,
# print the city name in camel case meaning first letter should be capital and rest in small.
#
# example : input : MYSORE ,  print - > Mysore

def capititlize_city(city):
    city = city[0].upper()+city[1:].lower()
    return city
print(capititlize_city(input()))


