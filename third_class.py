# multiplication table printer
#------------------- print the multiplication table upto 10 but skip the fifth iteration
print("enter the no.")
num = int(input())

for i in range(1,11):
    if i==5:
        continue
    print(num,"x",i,"=",num*i)