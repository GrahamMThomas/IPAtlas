
# *IPAtlas*

**IPAtlas** utilizes python's geoip2 library, Maxmind's free geolite2 database, and Basemap to create a map based on and IP list

Created by: **Graham Thomas**

## Features

The following **required** functionality is complete:
* [X] Parse through file and find latitude and longitude based on IP
* [X] Map IPs to a map using Basemap library

Potential future improvements:
* [X] Add IP labels to the map


## Video Walkthrough


![alt text](https://github.com/GrahamMThomas/IPAtlas/blob/master/IPAtlas_Example.gif "Demo")

GIF created with [LiceCap](http://www.cockos.com/licecap/).

## Library's Used
Basemap - https://matplotlib.org/basemap/

Maxmind's Database - http://dev.maxmind.com/geoip/geoip2/geolite2/

GeoIP2 - https://pypi.python.org/pypi/geoip2


## INSTALLATION

1. Install mpl_toolkits
`pip install --ignore-installed pyparsing --upgrade mpl_toolkits`

2. Then install Basemap using the instructions in the README
https://github.com/matplotlib/basemap

3. I was missing the dependency
`pip install pyproj`

4. Download ip_map.mmdb (GeoLite2 City Database binary/gzipped)
http://dev.maxmind.com/geoip/geoip2/geolite2/

5. Profit
