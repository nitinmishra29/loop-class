# factorial calculator
#-------------------- compute a factorial of a number using while loop
print('enter a number')
input_num = int(input())
factorial = 1

while input_num>0:
    factorial = factorial*input_num
    input_num -=1  #to drecrease the input num
print(factorial)