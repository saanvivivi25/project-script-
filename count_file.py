import os

print("Current Folder:", os.getcwd())

#open file
file = open(r"C:\Users\HP\Desktop\python-automation-internship\week 1\file.txt", "r")

# Read the entire content of the file
content = file.read()

# Count characters
char_count = len(content)

# Count words
word_count = len(content.split())

# Count lines
line_count = len(content.splitlines())

# Close the file
file.close()

# Display the results
print("Number of Lines:", line_count)
print("Number of Words:", word_count)
print("Number of Characters:", char_count)
