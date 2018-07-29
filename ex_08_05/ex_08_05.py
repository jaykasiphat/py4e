print("Assignment 8.5")

fhand = open("mbox-short.txt")
count = 0

for line in fhand:
    if line.startswith("From "):
        count = count + 1
        words = line.split() #split the words of the line into a list
        email = words[1] #access the 1st index to get the email address
        print(email)

print("There were", count, "lines in the file with From as the first word")
