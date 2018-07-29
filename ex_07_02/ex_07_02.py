print("Assignment 7.2")

# take user input as file name
fname = input("Enter file name: ")
# open the file using a file handle
try:
    fhand = open(fname)
except:
    print("Error, please try again")
else:
    count = 0
    total = 0
    # for everyline in the file
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence: "):
            x = line.strip()
            x = line.find(" ") #return the index of the space
            host = line[x+1:] #extract the number, from the " " index + 1, till the end of string
            host = float(host) #convert the num to float
            total = total + host
            count = count + 1
            average = total / count

    print("Total number of spam detection:", total)
    print("Average spam confidence:", average)
