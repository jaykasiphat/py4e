import re
'''
    Write a simple program to simulate the operation of the grep
    command on Unix. Ask the user to enter a regular expression
    and count the number of lines that matched the regular expression.
'''

print("Assignment 11.1")

fhand = open('mbox.txt')
regex = input("Enter a regular expression: ")

count = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall(regex, line)
    if len(x) < 1:
        continue
    else:
        count += 1

print("mbox.txt had", count, "lines that matched", regex)
