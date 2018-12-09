import xml.dom.minidom

file = xml.dom.minidom.parse('2860167.gpx')
file.normalize()

a = file.getElementsByTagName('time')
for e in a:
    print(e.firstChild.data)
