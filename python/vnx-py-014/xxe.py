# VNX-PY-014: XML External Entity injection
import xml.etree.ElementTree as ET

tree = ET.parse("config.xml")
root = tree.getroot()
data = ET.fromstring("<root>test</root>")
