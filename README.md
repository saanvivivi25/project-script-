This program was created and uploaded to GitHub as a simple file-handling project in Python. The objective of the program is to read a text file and calculate the total number of lines, words, and characters present in it. It also displays the current working directory using Python's os module.

How It Was Done
1.The os module was imported to access operating system functions.
2.The current working directory was displayed using os.getcwd().
3.The text file was opened in read mode ("r") using the open() function.
4.The entire content of the file was read and stored in a variable using file.read().
5.The number of characters was calculated using len(content).
6.The number of words was calculated by splitting the content into words using split() and then counting them with len().
7.The number of lines was calculated using splitlines() and len().
8.The file was closed using file.close().
9.Finally, the results were displayed using print() statements.

Outcome
The program successfully analyzes a text file and provides statistics about its contents, making it a useful beginner-level Python project for learning file handling, string operations, and basic automation.
