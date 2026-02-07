"""
Criteria:
    Use list comprehension to create a list of 100 random numbers from 1 to 10
    list_example = 10, 9, 2, 4, 1, 9, 2, ...

    print out the total elements in the list
    print out sum
    print out avg
"""

import random
#Using List comprehension
list_int = [random.randint(1,10) for x in range(100)]
total_sum = sum(list_int)
average_value=total_sum/len(list_int)

print(f"The total elements in the list are: {len(list_int)}")
print(f"The sum of all numbers in the list is: {total_sum}")
print(f"The average of all numbers in the list is: {average_value}")