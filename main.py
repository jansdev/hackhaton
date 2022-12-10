import numpy as np
import data_parsers
import AQI
import matplotlib.pyplot as plt

# from matplotlib import pyplot as plt

#print(data_parsers.parse_excel_data('2021_PM10_1g.xlsx', columns = ['PmGdyPorebsk', 'PmGdySzafran', 'PmSopBiPlowc', 'PmGdaWyzwole', 'PmGdaLeczkow', 'PmGdaPowWars']))
#print(data_parsers.parse_excel_data('2021_NO2_1g.xlsx', columns = ['PmGdyPorebsk', 'PmGdySzafran', 'PmSopBiPlowc', 'PmGdaWyzwole', 'PmGdaLeczkow', 'PmGdaPowWars']))
print(data_parsers.parse_excel_data('2021_CO_1g.xlsx', columns = ['PmGdyPorebsk', 'PmSopBiPlowc', 'PmGdaWyzwole', 'PmGdaLeczkow', 'PmGdaPowWars']))

CO_polution_3city_df = data_parsers.parse_excel_data('2021_CO_1g.xlsx', columns = ['PmGdyPorebsk-CO-1g', 'PmSopBiPlowc-CO-1g', 'PmGdaWyzwole-CO-1g', 'PmGdaLeczkow-CO-1g', 'PmGdaPowWars-CO-1g'])

#CO_polution_3city_df.plot(x='PmSopBiPlowc', y='PmGdyPorebsk')
#plt.show()