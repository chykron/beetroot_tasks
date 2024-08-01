"""
List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) where i goes from 1 to 10
and j is corresponding to i squared.
"""

my_tup_list = [(i, j) for i in range(1, 11) for j in [i ** 2]]
print(my_tup_list)
