##Solution Description##

1. I have used the set data structure in redies which will store the key value pairs and the property of the list is it will store the unique values and scard function is to count the length of set which finally gives the unique count of the food items.

2. I have used the nested loop to extract the data from the nutrition information after getting this information (Nutrition information is a JSON object again). This is a JSON information and this is a decoded information to get the unique data values the data values are pushed into the set and get the count using scard which will return the size of the set. This will return all the unique nutrition values present in the json.

3. I have used sorted hash table for performing this operation. This operation is used to add the value in the hash table which will add the unique values into the hash set and Zincrby is used to increment the number of times the values is been pushed into the hash table and this is auto sorted in the ascending order. I have extracted the first five elements from the sorted ascending order elements by using the command Zrange function which will give the first few of the elements with the maximum values.

4.  I have performed the average how many number of times the food product have repeated. In the numerator the value of the description is been repeated in the nutrient and in the denominator how many food items are present in the JSON file. 
I have extracted the nutrient value as a JSON formatted value and I have decoded the same and extracted the count of the number of times the food items repetitions by pushing the value in the set and I have pushed the ID of each of the line into the set and I have divided with this value to get the value of the average number of the repetitions.

5. I have stored all the values in the set into the MyList13 as requested in the assignment. I have pushed nutrition values into MyHash9. I have pushed the nutrition tag name into the TagNameSet hash table. I have inserted the value of the Id into the MainColl and corresponding nutrition's as a comma separated values. I have extracted these values using split function as in an array, I have pushed the value into the list of TagNameSet and get the related information based on the relation.
