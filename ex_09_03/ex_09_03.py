print("Exercise 9.3")

fname = input("Enter file name: ")
fhand = open(fname)

counts = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        mail = words[1]
        counts[mail] = counts.get(mail, 0) + 1

print(counts)
