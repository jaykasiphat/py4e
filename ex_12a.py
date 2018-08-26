from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

'''
    Assignment 12a: Scraping Numbers from HTML using BeautifulSoup.
    The program will use urllib to read the HTML from the data files below,
    and parse the data, extracting numbers and compute the sum of the numbers.
    http://py4e-data.dr-chuck.net/comments_42.html (2553)
    http://py4e-data.dr-chuck.net/comments_113032.html (2605)
'''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
html = urlopen(url, context=ctx).read()
# 1st argument - string; 2nd - how you’d like the markup parsed
x = BeautifulSoup(html, 'html.parser')

# Retrieve all span elements
total = 0
elements = x('span') # Give a list of all span tags
for element in elements:
    num = element.contents[0]
    num = int(num)
    total = total + num

print(total)
