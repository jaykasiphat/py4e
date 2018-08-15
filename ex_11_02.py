import re
'''
    Write a program to look for lines of the form `New Revision: 39772`.
    Extract the number from each of the lines using a regular expression and the findall() method.
    Compute the average of the numbers and print out the average.
'''

print("Exercise 11.2")
fname = input("Enter file name: ")
fhand = open(fname)

total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    num = re.findall('New Revision: ([0-9]+)', line)
    for n in num:
        n = float(n)
        total = total + n
        count += 1

avg = total / count
print("Average:", avg)
