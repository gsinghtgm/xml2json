import json
import sys

import xmltodict

"""
Created on 13.12.2017

@author: Gurparkash Singh <gsingh@tgm.ac.at>
@version: 20171312

@description: Umwandlung von einem xml File zu json.
"""
if ".xml" not in sys.argv[1]:
    print("Ungueltige Datei!")
else:
    with open(sys.argv[1], 'r') as f:  # Datei einlesen
        xmlString = f.read()
    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)  # wandelt von xml zu json

    jsonString = jsonString.replace("@", "attr-")  # replace @ mit attr-

    dateiname = sys.argv[1].replace(".xml", "") + ".json"  # Dateinamen to string

    print("\nJSON output(" + dateiname + "):")
    print(jsonString)

    with open(dateiname, 'w') as f:
        f.write(jsonString)
