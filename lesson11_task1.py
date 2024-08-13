"""
Write a script that creates a new output file called my_file.txt and writes the string "Hello file world!" in it.
Then write another script that opens my_file.txt, and reads and prints its contents.
Run your two scripts from the system command line.
"""

# Step 1: Write to the file
with open("my_file.txt", "w") as file:
    file.write("Hello file world!\n")

# Step 2: Read from the file and print the contents
with open("my_file.txt", "r") as file:
    content = file.read()

print(content)
