# sum of even numbers
#----------- calculate sum of even numbers upto a given numbers n

n = int(input("enter the numbers n: "))
sum_even=0

for i in range(1,n+1):
    if (i%2==0):
        sum_even+= 1

print (sum_even)