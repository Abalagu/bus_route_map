import json

with open(r'..\asset\route_26.json', 'r') as f:
    points = json.loads(f.read())
    path_points = [(p['Longtitude'], p['Latitude']) for p in points]