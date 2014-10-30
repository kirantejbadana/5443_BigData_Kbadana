1. I have used the set data strucure in redies which will store the key value pairs and the property of the list is it will store the unique values and scard function is to count the length of set which finally gives the unique count of the food items.

2. I have used the nested loop to extract the data from the nutrition information after getting this informaytion. This is a lJSON information and this is a decoded information to get the unique data values the data values are puhed into the set and get the count using scard which will return the the size of the set. This will return all the unique nutrition values present in the json.

3. I have used sorted hash table for performing this operation. This operation is used to add the value in the hash table which will add the unique values into the hash set and zincrby is used to increment the number of times the values is been pushed into the hash table and this is auto sorted in the desecnding order. I have extracted the first five elements from the sorted ascending order elements by using the command Zrange function which will give the first few of the elements with the maximum values.

4.  I have performed the avarage how many number of times the food product have repeated. In the numarator the value of the description is been repeated in the nutriion and in the denominator hoe many food items are present in the JSON file. 
