from lxml import etree
from functions.set_placemark import kml_gen_points

kml = etree.Element('kml')
kml.set('xmlns', "http://www.opengis.net/kml/2.2")
Placemark = kml_gen_points('simple', 'description here', '-122,37.73')
kml.append(Placemark)

s = etree.tostring(kml, pretty_print=True)
print(s.decode())
