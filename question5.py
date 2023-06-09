# 5- write a program which takes the name of the user as input and print the index of character 'a' in the string.
# if 'a' is not there then return -1.

def print_index_a(name):
    if ((name.find('a'))==-1):
        print(-1)
        return
    count=0
    for i in name:
        if i =='a':
            print(count)
            count+=1
        else:
            count+=1


print_index_a(input())