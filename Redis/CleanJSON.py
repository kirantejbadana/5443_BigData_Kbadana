# This code is able to decode till line number 338
import redis
import string
import json
import sys

#Link up with redis
r = redis.Redis(host='localhost', port=6379, db=0)
# Open nutrition.json for reading and put the reference in 'f'
f = open('nutrition.json','r')
def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char
# Read each line from f placing one line into jline at every iteration
for jline in f:
	filtered_data=filter(onlyascii, jline)
	jline = json.loads(filter(lambda x: x in string.printable, jline))
	print jline