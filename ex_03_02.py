print("Running 3.2 assignment..")

try:
    hrs = float(input("Enter Hours: "))
    rph = float(input("Enter Rate Per Hour: "))
except:
    print("Error, please enter numeric input")
else:
    if hrs > 40:
        gross_pay = (40 * rph) + (hrs - 40) * rph * 1.5
    else:
        gross_pay = hrs * rph
    print("Pay:", gross_pay)
