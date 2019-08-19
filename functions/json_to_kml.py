import json
from lxml import etree
from functions.kml_process import json_to_points, kml_gen_stop_points, kml_gen_path_points


def generate_kml(json_file, kml_file):
    """
    from bus route info to kml file
    :param json_file:
    :param kml_file:
    """
    f = open(json_file, 'r')
    points = json.loads(f.read())
    stop_points, path_points = json_to_points(points)
    folder_stop_points = kml_gen_stop_points(stop_points)
    folder_path_points = kml_gen_path_points(path_points)

    kml = etree.Element('kml')
    kml.set('xmlns', "http://www.opengis.net/kml/2.2")
    Document = etree.SubElement(kml, 'Document')
    Document.append(folder_stop_points)
    # Document.append(folder_path_points)

    s = etree.tostring(kml, pretty_print=True)
    # print(s.decode())

    with open(kml_file, 'wb') as fwrite:
        fwrite.write(s)

