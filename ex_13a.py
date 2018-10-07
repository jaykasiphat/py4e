import urllib.request
import json

'''
    The program will prompt for a URL, read the JSON data from that URL using urllib,
    and then parse and extract the comment counts from the JSON data,
    compute the sum of the numbers in the file.

    Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_113035.json (Sum ends with 41)
'''

url = input('Enter URL: ')
connection = urllib.request.urlopen(url)
data = connection.read().decode() #string from utf-8 to unicode
js = json.loads(data) #deserialize 'data' to a Python object
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

total = 0
count = 0
for item in js['comments']:
    num = item['count']
    total = total + num
    count += 1

print('Count:', count)
print('Sum:', total)
