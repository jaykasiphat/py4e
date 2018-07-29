print("Assignment 5.2")

largest = None
smallest = None

#Set up a loop and prompt user for input
#Convert str to int
#Check for "done" and invalid input 
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
        except:
            print("Invalid input")
            continue

    #Find the largest number
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    #Find the smallest number
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
