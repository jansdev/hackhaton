import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from mpl_toolkits.basemap import Basemap
import pandas as pd
import io


def polutionHistogram(classmethod):
    plt.hist(classmethod, 
    weights=np.ones(len(classmethod)) / len(classmethod))
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    return plt

def mapPlot():

    #polution points data
    lat = [54.560836, 
        54.465758, 
        54.43451, 
        54.400833, 
        54.380279, 
        54.353336]
    
    lon = [18.493331, 
        18.464911, 
        18.57884, 
        18.657497, 
        18.620274, 
        18.635283]

    # determine range to print based on min, max lat and lon of the data
    margin = 0.1 # buffer to add to the range
    lat_min = min(lat) - margin
    lat_max = max(lat) + margin
    lon_min = min(lon) - margin
    lon_max = max(lon) + margin

    # create map using BASEMAP
    m = Basemap(llcrnrlon=lon_min,
                llcrnrlat=lat_min,
                urcrnrlon=lon_max,
                urcrnrlat=lat_max,
                lat_0=(lat_max - lat_min)/2,
                lon_0=(lon_max-lon_min)/2,
                projection='merc',
                resolution = 'h',
                area_thresh=10000.,
                )
    m.drawcoastlines()
    m.drawcounties()
    m.drawmapboundary(fill_color='#46bcec')
    m.fillcontinents(color = 'white',lake_color='#46bcec')
    # convert lat and lon to map projection coordinates
    lons, lats = m(lon, lat)
    # plot points as red dots
    m.scatter(lons, lats, marker = 'o', color='r', zorder=5)
    
    return plt