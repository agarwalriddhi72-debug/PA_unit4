"""
Criteria:
    Use list comprehension to create a list of 100 random numbers from 1 to 10
    list_example = 10, 9, 2, 4, 1, 9, 2, ...

    print out the total elements in the list
    print out sum
    print out avg
"""

import random
counter = 0
list_int = []
total_sum = 0

#stores 100 random numbers in the list
while counter<100:
    list_int.append(random.randint(0,10))
    counter+=1

#Adds all numbers in list together
for number in list_int:
    total_sum+=number
    counter+=1

average_value=total_sum/len(list_int)

print(f"The total elements in the list are: {len(list_int)}")
print(f"The sum of all numbers in the list is: {total_sum}")
print(f"The average of all numbers in the list is: {average_value}")