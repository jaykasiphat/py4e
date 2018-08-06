print("Assignment 6.5")

text = "X-DSPAM-Confidence:    0.8475"

# x returns the index of the number 0
x = text.find("0")
print(x)

# extracting the number from the 23rd index to the end of string
# convert to float
y = float(text[x:])
print(y)
