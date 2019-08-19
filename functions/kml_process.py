from pyproj import Proj, transform
from lxml import etree


def mercator_to_lonlat(x1, y1):
    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')
    x2, y2 = transform(inProj, outProj, x1, y1)
    return '{},{}'.format(x2, y2)


def kml_gen_points(point_coordinates, point_name='', point_style='', point_description=''):
    # construction

    # -Placemark
    #     -name
    #     -styleUrl
    #     -description
    #     -Point
    #         -coordinates

    placemark = etree.Element('Placemark')
    name = etree.SubElement(placemark, 'name')
    style_url = etree.SubElement(placemark, 'styleUrl')
    description = etree.SubElement(placemark, 'description')
    point = etree.SubElement(placemark, 'Point')
    coordinates = etree.SubElement(point, 'coordinates')

    # value assignment
    name.text = point_name
    style_url.text = point_style
    description.text = point_description
    coordinates.text = point_coordinates

    return placemark


def json_to_points(points):
    """
    points consist of way point and stop point.
    extract stop points from all provided points, including name, stop code, and lon-lat info
    for path generation, lon-lat pair info for all points are extracted
    :param points:
    :return:
    """
    # stop_points_prep = [p for p in points if p['Name'] != 'Way Point']
    stop_points = [{
        'Name': p['Name'],
        'StopCode': p['Stop']['StopCode'],
        'IsTimePoint': p['Stop']['IsTimePoint'],
        'lonlat': mercator_to_lonlat(p['Longtitude'], p['Latitude'])
    } for p in points if p['Name'] != 'Way Point']

    path_points = [mercator_to_lonlat(p['Longtitude'], p['Latitude']) for p in points]

    return stop_points, path_points


def kml_gen_stop_points(stop_points):
    folder = etree.Element('Folder')
    for stop in stop_points:
        if stop['IsTimePoint']:
            placemark = kml_gen_points(stop['lonlat'], stop['Name'], 'time_point', 'Time Point')
        else:
            placemark = kml_gen_points(stop['lonlat'], stop['Name'], 'non_time_point', 'Not Time Point')
        folder.append(placemark)
    return folder


def kml_gen_path_points(path_points):
    pass
