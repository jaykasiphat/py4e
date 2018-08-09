print("Exercise 8.6")

ls = []
# Method 1
# while True:
#     num = input("Enter a number: ")
#     if num != "done":
#         num = float(num)
#         ls.append(num)
#     else:
#         break

# Method 2
# while True:
#     num = input("Enter a number: ")
#     if num != "done":
#         try:
#             num = float(num)
#         except:
#             print("Error, please try again")
#         else:
#             ls.append(num)
#     else:
#         break

# Method 3
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = float(num)
        except:
            print("Error, please try again")
        else:
            ls.append(num)

max_num = max(ls)
min_num = min(ls)
print(ls)
print("Maximum:", max_num)
print("Minimum:", min_num)
