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

58M Sep 10 10:36 GpsFilePoints.csv
58M Sep 11 09:20 GpsFilePoints.csv.gz
58M Sep 11 08:53 GpsFilePoints.csv.zip
467M Sep 10 10:39 GpsFilePoints.sql
60M Sep 11 09:21 GpsFilePoints.sql.gz
60M Sep 11 08:57 GpsFilePoints.sql.zip
2.3G Sep  2 18:24 GpsFilePoints.xml
75M Sep 11 09:22 GpsFilePoints.xml.gz
75M Sep 11 08:55 GpsFilePoints.xml.zip
771M Sep  2 19:09 GpsFilePoints.yml
61M Sep 11 09:23 GpsFilePoints.yml.gz
61M Sep 11 08:59 GpsFilePoints.yml.zip

