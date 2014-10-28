import redis
import string
import json
import sys

#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)
r.flushdb()
f = open('nutrition.json','r')
# Read one line from file

for line in f:
	line = json.loads(filter(lambda x: x in string.printable, line))
	for FoodItmVal in line['nutrients']:
		r.zincrby('Test11',FoodItmVal['tagname'],1)
	r.sadd('Test12',line['_id'])
Set5Count=r.scard('Test12')
Food_Item = 'PROCNT'
FoodItmScr=r.zscore('Test11',Food_Item)
print FoodItmScr
print Set5Count
print float(FoodItmScr)*100/float(Set5Count)