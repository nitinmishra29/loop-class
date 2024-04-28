#check prime number
#--------- check if numberis prime
number = int(input('enter a no to check it is primeno. or not: '))

if number>1:
    for i in range(2,number):
        if(number%i==0):
            print("the" ,number,'is not prime no.')
            break
        else:
            print("the no is prime no")
            break