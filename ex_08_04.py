print("Assignment 8.4")

fhand = open("romeo.txt")
pieces = list()

for line in fhand:
    words = line.strip()
    words = line.split() #split the words of the line into a list
    #print(words)
    for word in words: #for each word in the list of words
        if word not in pieces:
            pieces.append(word) #add the word if the word isn't in pieces
    pieces.sort()

print(pieces)
