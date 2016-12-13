# -*- coding: utf-8 -*-
"""Trip_Toute_Mapper.py: Script for drawing specified trip route on map projection

__author__ = "Jason M. Battle"
"""
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

FROM = 'Incheon'
TO = 'Chiang Mai'
PROJ = 'ortho'
RESOL = 'c'
COLOR = 'red'

# Find lat/long Coordinates
locator = Nominatim(proxies={'https':'168.219.61.252:8080'})
from_loc = locator.geocode(FROM, timeout=10)[-1]
to_loc = locator.geocode(TO, timeout=10)[-1]

fig = plt.figure(figsize=(16,9))
bmap = Basemap(projection=PROJ, resolution=RESOL, lat_0=((from_loc[0] + to_loc[0]) / 2.), lon_0=(from_loc[1] + to_loc[1]) / 2.)
bmap.drawcoastlines()
bmap.drawmapboundary(fill_color='blue')
bmap.drawcountries()
bmap.fillcontinents(color='green', lake_color='blue')
bmap.drawgreatcircle(from_loc[1], from_loc[0], to_loc[1], to_loc[0], color=COLOR, linewidth=2)
x,y = bmap(from_loc[1], from_loc[0])
bmap.plot(x,y, color=COLOR, marker='o')
plt.text(x, y-300000, FROM, color='red', weight='bold')
x,y = bmap(to_loc[1], to_loc[0])
bmap.plot(x,y, color=COLOR, marker='o')
plt.text(x, y-300000, TO, color='red', weight='bold')
