from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import geoip2.database

map = Basemap()

# Uncomment for a different look
# map.drawcoastlines()
# map.drawcountries()

map.fillcontinents(color='#ffe0b3')
map.drawmapboundary()

lons = []
lats = []
labels = []
reader = geoip2.database.Reader('ip_map.mmdb')

fin = open("input.txt", "r")
for ip in fin:
    response = reader.city(ip.strip())
    labels.append(ip.strip())
    lats.append(response.location.latitude)
    lons.append(response.location.longitude)
    print "{} -- {}, {}".format(ip.strip(),
                                response.location.latitude,
                                response.location.longitude)

x, y = map(lons, lats)
map.plot(x, y, 'bo', markersize=3, color='red')

plt.show()
