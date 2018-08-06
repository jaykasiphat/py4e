print("Exercise 9.5")

fname = input("Enter file name: ")
fhand = open(fname)

counts = dict()
for line in fhand:
    words = line.split()
    if line.startswith("From "):
        mail = words[1]
        ncount = mail.find("@")
        email = mail[ncount:]
        counts[email] = counts.get(email, 0) + 1

print(counts)
