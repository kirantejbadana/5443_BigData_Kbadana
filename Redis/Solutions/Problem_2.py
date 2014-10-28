import redis
import sys
import json
import string


r=redis.StrictRedis(host='localhost',port=6379,db=0)

def is_json(myjson):
	try:
		json_object=json.loads(myjson)
	except ValueError,e:
		return False
	return True

f=open('nutrition.json','r')

for line in f:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		nutrients=line['nutrients']
		for nutrient in nutrients:
			r.sadd("MyList",nutrient['_id'])
print r.scard("MyList")