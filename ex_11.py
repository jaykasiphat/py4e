import re

'''
    Read through and parse a file with texts and numbers.
    Extract all the numbers in the file and compute the
    sum of the numbers.
'''

print("Assignment 11")

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Error, invalid input")
    quit()

sum = 0
count = 0
for line in fhand:
    num = re.findall('[0-9]+', line) #one or more digits from 0 - 9
    for n in num:
        n = int(n)
        sum = sum + n
        count += 1
        print(count, ":", n) #check for the total

print("Sum =", sum)
