print("Assignment 10.2")

fhand = open('mbox-short.txt')

counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time[:2]
        counts[hour] = counts.get(hour, 0) + 1

print(counts)

for k, v in sorted(counts.items()):
    print(k, v)
