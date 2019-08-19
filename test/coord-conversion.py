from functions.kml_process import mercator_to_lonlat

x1, y1 = -10724489.831063235, 3582762.3901209766
lonlat = mercator_to_lonlat(x1, y1)
print(lonlat)
