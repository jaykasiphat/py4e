print("Assignment 5.1")

#Set count as the counter
#Set total as the accumulator
count = 0
total = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = float(num)
        except:
            print("Invalid input")
            continue

    total = total + num
    count = count + 1
    average = total / count

print("Total: ", total)
print("Count: ", count)
print("Average: ", average)
