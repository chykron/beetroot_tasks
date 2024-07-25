"""
String manipulation:
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: 'x'
Expected Result: Empty String
"""

my_string = 'helloworld'

if len(my_string) == 4:
    print(my_string)
elif len(my_string) > 4:
    print(my_string[:2] + my_string[-2:])
elif len(my_string) == 2:
    print(my_string + my_string)
else:
    print('')
