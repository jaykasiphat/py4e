print("Exercise 9.2")

fname = input("Enter file name: ")
fhand = open(fname)

count = dict()
for line in fhand:
    words = line.split()
    if len(words) > 3 and line.startswith("From"):
        day = words[2]
        count[day] = count.get(day, 0) + 1
    else:
        continue

print(count)
