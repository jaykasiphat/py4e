print("Assignment 7.1")

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Error, please try again")
    quit()

for line in fhand:
    line = line.strip()
    line = line.upper()
    print(line)
