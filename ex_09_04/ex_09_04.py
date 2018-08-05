print("Assignment 9.4")

fhand = open('mbox-short.txt')

counts = dict() #create a dictionary
for line in fhand:
    if line.startswith("From "):
        words = line.split() #split the words of the line into a list
        mail = words[1] #extract the email address
        counts[mail] = counts.get(mail, 0) + 1 #make a histogram

bigkey = None
bigcount = None
for key,value in counts.items():
    if bigkey is None or value > bigcount:
        bigkey = key
        bigcount = value

print(bigkey, bigcount)
