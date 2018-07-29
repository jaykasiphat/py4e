print("Running 3.1 assignment..")

hrs = float(input("Hours: "))
rph = float(input("Rate Per Hour: "))

if hrs > 40:
    gross_pay = (40 * rph) + (hrs - 40) * rph * 1.5
else:
    gross_pay = hrs * rph
print(gross_pay)
