#  validate input
#----- kkep asking a input from user until they enter a number betwwen 1 to 10

while True:
    print('enter a no. between 1 to 10')
    number=int(input())
    if 1<= number <=10:
        print('the no is between 1 and 10')
        break
    else:
        print('enter a no. between 1 to 10')
        break
