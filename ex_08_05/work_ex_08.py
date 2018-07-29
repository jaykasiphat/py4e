print("Worked Exercise Chapter 8")

fhand = open("mbox-short.txt")

for line in fhand:
    line = line.strip()
    words = line.split()
    #guardian in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        pieces = words[2]
    print(pieces)
