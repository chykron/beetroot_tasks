"""
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""
from random import randint

my_list1 = []
my_list2 = []
# my_list3 = []

length = 0

while length < 10:
    # generate random numbers for each list
    num1 = randint(1, 10)
    num2 = randint(1, 10)

    # append those numbers to each list
    my_list1.append(num1)
    my_list2.append(num2)

    # # check for common integers without duplicates
    # if num1 == num2 and num1 not in my_list3:
    #     my_list3.append(num1)
    length += 1

my_list3 = set(my_list1) ^ set(my_list2)

print(list(my_list3))
