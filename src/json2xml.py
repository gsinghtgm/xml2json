import json
import sys

import xmltodict

"""
Created on 13.12.2017

@author: Gurparkash Singh <gsingh@tgm.ac.at>
@version: 20171312

@description: Umwandlung von einem json File zu xml.
"""
if ".json" not in sys.argv[1]:
    print("Ungueltige Datei!")
else:
    with open(sys.argv[1], 'r') as f:  # Datei einlesen
        jsonString = f.read()
    jsonString = jsonString.replace("attr-", "@")  # replace  attr- mit @

    dateiname = sys.argv[1].replace(".json", "") + ".xml"#Dateinamen to string

    xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True) #wandelt von json zu xml
    print("\nXML output("+dateiname+"):")
    print(xmlString)

    with open(dateiname, 'w') as f:
        f.write(xmlString)
