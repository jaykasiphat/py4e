print("Running 3.3 assignment..")

try:
    score = float(input("Enter Score: "))
except:
    print("Error, please enter numeric input")
else:
    if score > 1.0 or score < 0.0:
        print("Score must be a value between 0.0 and 1.0")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
