"""
The valid phone number program:

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""

while True:
    phone_number = input("Your phone number, please: ")
    if len(phone_number) == 10 and phone_number.isdigit():
        print("Thanks for providing with your phone number")
        break
    else:
        print("You phone number should contain 10 digit characters, please try again")
        continue
