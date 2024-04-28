# list uniquene ss check
#-- check the all element in list is unique if it duplicate found exit the loop and print the duplicate
# items=['apple', 'orange', 'banana','mango', 'apple']


items=['apple', 'orange', 'banana','mango', 'apple']

unique_items=set()

for item in items:
    if item in unique_items:
        print("duplicate", item)
    else:
        unique_items.add(item)
 