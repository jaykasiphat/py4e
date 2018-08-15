print("Exercise 10.3")

#prints the letters from a-z in decreasing order of frequency

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Error, invalid file")
    quit()

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

counts = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter in alphabets:
                counts[letter] = counts.get(letter, 0) + 1
            else:
                continue

ls = list()
for letter, count in counts.items():
    newtup = (count, letter)
    ls.append(newtup)

ls = sorted(ls, reverse = True)

num = 0
for count, letter in ls:
    num = num + 1 #Makes sure it counts to 26 alphabets
    print(letter, count)

print(ls[:5])
print(num)
