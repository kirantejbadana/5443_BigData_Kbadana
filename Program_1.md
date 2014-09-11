##Converting XML to JSON##

As per my understanding size of the file is not the only thing that bothers for reading the data but also how well the file is been organized. I believe, form the file formats provided XML is one which provides the data in much more organized way and we have been provided with lot of options for reading the data from the XML by Microsoft.
<ol>
<li> XmlTextReader </li>
<li> XmlDocument </li>
<li> XPathDocument </li>
<li> XmlSerializer</li>
<li> DataSet </li>

###Steps To Be Followed ###

I will use the below set of lines for converting the XML file to JSON file format
```

XmlDocument doc = new XmlDocument();
doc.LoadXml(xml);
string jsonText = JsonConvert.SerializeXmlNode(doc);
```

After converting each line I will send this to the JSON file for getting the JSON format. Here I will be using the pre-existing file converters for making the conversions.


Before making the conversion I will use the XSD file to check if the XML file is well formatted or not. I will parse the XML using the pre defined parsed present in the Visual Studio

###Coompressing the files###

Compressing the files made the file size reduce

58M Sep 10 10:36 GpsFilePoints.csv <br>
58M Sep 11 09:20 GpsFilePoints.csv.gz <br>
58M Sep 11 08:53 GpsFilePoints.csv.zip <br>
467M Sep 10 10:39 GpsFilePoints.sql <br>
60M Sep 11 09:21 GpsFilePoints.sql.gz <br>
60M Sep 11 08:57 GpsFilePoints.sql.zip <br>
2.3G Sep  2 18:24 GpsFilePoints.xml <br>
75M Sep 11 09:22 GpsFilePoints.xml.gz <br>
75M Sep 11 08:55 GpsFilePoints.xml.zip <br>
771M Sep  2 19:09 GpsFilePoints.yml <br>
61M Sep 11 09:23 GpsFilePoints.yml.gz <br>
61M Sep 11 08:59 GpsFilePoints.yml.zip <br>


| Type | Description                                  | Size    | After Compression   |
|------|----------------------------------------------|---------|---------------------|
| csv  |Comma seperated values                        | 484MB   |   58M               |
| sql  |Structured Query Language (insert statements) | 467MB   |   60M               |
| xml  |EXtensible Markup Language                    | 2.3GB   |   75M               |
| yaml |Yet Another Markup Language                   | 771MB   |   61M               |
