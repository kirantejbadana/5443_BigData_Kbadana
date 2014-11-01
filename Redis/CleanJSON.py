# This code is able to decode till line number 338
import redis
import string
import json
import sys

def is_json(myjson):
	try:
		json_object=json.loads(myjson)
	except ValueError,e:
		return False
	return True
#Link up with redis
#r = redis.Redis(host='localhost', port=6379, db=0)
# Open nutrition.json for reading and put the reference in 'f'
f = open('nutrition.json','r')
g = open('Output.json','w')
def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char
lineNum=0
decLineNum=0
# Read each line from f placing one line into jline at every iteration
for jline in f:
	filtered_data=filter(onlyascii, jline)
	if is_json(jline):
		jline = json.loads(filter(lambda x: x in string.printable, jline))
		print jline
		decLineNum=decLineNum+1
		g.write(str(jline))
		print "##################################\n"
		print decLineNum
		print "\n##################################\n"
	lineNum=lineNum+1
	print  "********************************\n"
	print lineNum
	print  "\n********************************\n"
	
