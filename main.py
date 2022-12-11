from data_models import TricityPM10PoluttionModel
from data_models import TricityNO2PoluttionModel
from data_models import TricityCOPoluttionModel
from plot_functions import polutionHistogram
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig, ax = plt.subplots(figsize=(12, 8))

m = Basemap(projection='gnom', lat_0=54.27, lon_0=18.34,
            width=120000, height=120000, resolution='h', ax=ax)
m.fillcontinents(color="#FFDDCC", lake_color='#DDEEFF')
m.drawmapboundary(fill_color="#DDEEFF")
m.drawcoastlines()
ax.set_title("Mapa Trójmiasta")

plt.show()


#polutionHistogram(TricityPM10PoluttionModel.pm_gda_leczkow)
