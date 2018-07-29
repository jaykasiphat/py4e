print("Assignment 4.6")

# ver.5
def computepay(hrs, rph):
    try:
        hrs = float(hrs)
        rph = float(rph)
    except:
        print("Please enter a number")
    else:
        if hrs > 40:
            gross_pay = ((40 * rph)) + ((hrs - 40) * rph * 1.5)
            return gross_pay
        else:
            gross_pay = hrs * rph
            return gross_pay

hour = input("Enter hours: ")
rate = input("Enter rate per hour: ")
print(computepay(hour, rate))

# ver.1
# def computepay(hrs, rph):
#     if hrs > 40:
#         gross_pay = ((40 * rph)) + ((hrs - 40) * rph * 1.5)
#         return gross_pay
#     else:
#         gross_pay = hrs * rph
#         return gross_pay

# ver.2
# def computepay(hrs, rph):
#     try:
#         hrs = float(input("Enter hours: "))
#         rph = float(input("Enter rate per hour: "))
#     except:
#         print("Please enter a number")
#     else:
#         if hrs > 40:
#             gross_pay = ((40 * rph)) + ((hrs - 40) * rph * 1.5)
#             return gross_pay
#         else:
#             gross_pay = hrs * rph
#             return gross_pay
#
# print(computepay(45, 10.5))

# ver.3
# def computepay(hrs, rph):
#     try:
#         if hrs > 40:
#             gross_pay = ((40 * rph)) + ((hrs - 40) * rph * 1.5)
#             return gross_pay
#         else:
#             gross_pay = hrs * rph
#             return gross_pay
#     except:
#         print("Please enter a number")
#
# print(computepay(45, 10.5))

# ver.4
# def computepay(hrs, rph):
#     try:
#         if hrs > 40:
#             gross_pay = ((40 * rph)) + ((hrs - 40) * rph * 1.5)
#             return gross_pay
#         else:
#             gross_pay = hrs * rph
#             return gross_pay
#     except:
#         print("Please enter a number")
#
# hour = float(input("Enter hours: "))
# rate = float(input("Enter rate per hour: "))
# print(computepay(hour, rate))
