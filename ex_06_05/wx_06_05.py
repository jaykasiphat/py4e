print("Worked Exercise 6.5")

text = "X-DSPAM-Confidence: 0.8475"
x = text.find(":")
print(x)
y = text[x+1:]
print(y)
z = float(text[x+1:])
print(z)
