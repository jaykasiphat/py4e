import urllib.request
import xml.etree.ElementTree as ET

'''
Write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL using urllib
and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_113034.xml (Sum ends with 53)
'''

#Method 1
url = input('Enter url: ')
xml = urllib.request.urlopen(url).read()
print('Retrieving', url)
print('Retrieved', len(xml), 'characters')

#parses XML from a string directly into the root Element of the parsed tree.
root = ET.fromstring(xml)

#use an XPath selector string look through the entire tree of XML for any tag named 'count'
lst = root.findall('.//count')
print('Count:', len(lst))

total = 0
for item in lst:
    total = total + int(item.text) #within item, grab the text content
print('Sum:', total)

# Method 2
# url = input('Enter url: ')
# xml = urllib.request.urlopen(url).read()
# print('Retrieving', url)
# print('Retrieved', len(xml), 'characters')
#
# root = ET.fromstring(xml)
#
# total = 0
# count = 0
# for num in root.findall('.//count'):
#     count += 1
#     total = total + int(num.text)
# print('Count:', count)
# print('Sum:', total)
