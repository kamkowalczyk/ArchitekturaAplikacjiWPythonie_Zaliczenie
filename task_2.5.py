import requests
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/cd_catalog.xml"

response = requests.get(url)
data = response.content

root = ET.fromstring(data)

tracks = []

for cd in root.findall('CD'):
    artist = cd.find('ARTIST').text
    title = cd.find('TITLE').text
    tracks.append((artist, title))

for track in tracks:
    print(track)