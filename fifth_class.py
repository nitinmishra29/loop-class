# Find the first non repeater character
#------ given a string find a first non repeated character
print('Enter  a string')
input_string=input()

for char in input_string:
    print(char)
    if input_string.count(char)==1:
        print( "the character is",char)
        break