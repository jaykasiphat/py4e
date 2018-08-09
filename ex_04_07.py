print("Exercise 4.7")

def computegrade(score):
    try:
        score = float(score)
    except:
        return "Invalid input: please enter a numeric input"

    if score > 1:
        return "Invalid input: score must be less than 1.0"
    else:
        if score > 0.9:
            return "A"
        elif score > 0.8:
            return "B"
        elif score > 0.7:
            return "C"
        elif score > 0.6:
            return "D"
        else:
            return "F"

grade = input("Enter score: ")
print(computegrade(grade))
