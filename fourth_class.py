#  Reverse a string using the loop

print("Enter a string")
input_string =input()
reserved_string=""

for char in input_string:
    reserved_string= char+reserved_string
    print(reserved_string)
      