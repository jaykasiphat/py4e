print("Exercise 10.1")
'''
    Read the file and parse the "From " lines and pull
    out the addresses. Count a number of messages from
    each person using a dictionary. Print the person
    with the most commits by creating a list of tuples
    from the dictionary. Sort the list in a reverse order.
'''

fname = input("Enter file name: ")
fhand = open(fname)

counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        mail = words[1]
        counts[mail] = counts.get(mail, 0) + 1
        # print(counts)

ls = list()
for email, count in counts.items():
    newtup = (count, email)
    ls.append(newtup)

ls = sorted(ls, reverse=True)

for count, email in ls[:1]:
    print(email, count)
