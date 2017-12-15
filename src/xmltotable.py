import sys
import lxml.etree as et
"""
Created on 13.12.2017

@author: Gurparkash Singh <gsingh@tgm.ac.at>
@version: 20171312

@description: xml file pretty readble.
"""
if ".xml" not in sys.argv[1]:
    print("Ungueltige Datei!")
else:
    doc = et.parse(sys.argv[1])
    for element in doc.findall("book"):
        print(element.find("author").text + " " +
              element.find("year").text +
              ", EUR" + element.find("price").text)

