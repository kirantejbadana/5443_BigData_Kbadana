I have developed this for cleaning the JSON file. Initally I was able to process the file till 2700 lines and there was an json decoding error and I am not able to predict what it is. Just to find out how many lines are good as JSON after the decoding and I have found surprising results as mentioned below:

Number of Lines:

nutrition.json -> 8196
Output.json -> 8194

Size of the File:

nutrition.json -> 66 MB
Output.json -> 67 MB

I am still not able to understand how come the file size of output file is still greater than the size of the input file inspite of removing the special charecters and two lines of JSON objects.
