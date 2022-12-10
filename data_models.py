import data_parsers
import numpy as np

#all data models we perform analysis on

#model that contains PM10 polution data as numpy arrays
class TricityPM10PoluttionModel:

    #data source parameters 
    file_name = 'data/2021_PM10_1g.xlsx'
    column_names = ['Kod stacji', 'PmGdyPorebsk', 'PmGdySzafran', 'PmSopBiPlowc', 'PmGdaWyzwole', 'PmGdaLeczkow', 'PmGdaPowWars']

    #parse data
    tricity_pm10_pollution_data = data_parsers.parse_excel_data(file_name, column_names)       

    #define class parameters
    timestamps = tricity_pm10_pollution_data[column_names[0]].to_numpy()
    timestamps = np.delete(timestamps, [0, 1, 2 , 3]) 

    pm_gdy_porebsk = tricity_pm10_pollution_data[column_names[1]].to_numpy()
    pm_gdy_porebsk = np.delete(pm_gdy_porebsk, [0, 1, 2 , 3]) 

    pm_gdy_szafran = tricity_pm10_pollution_data[column_names[2]].to_numpy()
    pm_gdy_szafran = np.delete(pm_gdy_szafran, [0, 1, 2 , 3]) 

    pm_sop_bi_plowc = tricity_pm10_pollution_data[column_names[3]].to_numpy()
    pm_sop_bi_plowc = np.delete(pm_sop_bi_plowc, [0, 1, 2 , 3]) 

    pm_gda_wyzwole = tricity_pm10_pollution_data[column_names[4]].to_numpy()
    pm_gda_wyzwole = np.delete(pm_gda_wyzwole, [0, 1, 2 , 3]) 
    
    pm_gda_leczkow = tricity_pm10_pollution_data[column_names[5]].to_numpy()
    pm_gda_leczkow = np.delete(pm_gda_leczkow, [0, 1, 2 , 3]) 

    pm_gda_pow_wars = tricity_pm10_pollution_data[column_names[6]].to_numpy()
    pm_gda_pow_wars = np.delete(pm_gda_pow_wars, [0, 1, 2 , 3]) 

#model that contains NO2 polution data as numpy arrays
class TricityNO2PoluttionModel:

    #data source parameters 
    file_name = 'data/2021_NO2_1g.xlsx'
    column_names = ['Kod stacji', 'PmGdyPorebsk', 'PmGdySzafran', 'PmSopBiPlowc', 'PmGdaWyzwole', 'PmGdaLeczkow', 'PmGdaPowWars']

    #parse data
    tricity_no2_pollution_data = data_parsers.parse_excel_data(file_name, column_names)       

    #define class parameters
    timestamps = tricity_no2_pollution_data[column_names[0]].to_numpy()
    timestamps = np.delete(timestamps, [0, 1, 2 , 3]) 

    pm_gdy_porebsk = tricity_no2_pollution_data[column_names[1]].to_numpy()
    pm_gdy_porebsk = np.delete(pm_gdy_porebsk, [0, 1, 2 , 3]) 

    pm_gdy_szafran = tricity_no2_pollution_data[column_names[2]].to_numpy()
    pm_gdy_szafran = np.delete(pm_gdy_szafran, [0, 1, 2 , 3]) 

    pm_sop_bi_plowc = tricity_no2_pollution_data[column_names[3]].to_numpy()
    pm_sop_bi_plowc = np.delete(pm_sop_bi_plowc, [0, 1, 2 , 3]) 

    pm_gda_wyzwole = tricity_no2_pollution_data[column_names[4]].to_numpy()
    pm_gda_wyzwole = np.delete(pm_gda_wyzwole, [0, 1, 2 , 3]) 
    
    pm_gda_leczkow = tricity_no2_pollution_data[column_names[5]].to_numpy()
    pm_gda_leczkow = np.delete(pm_gda_leczkow, [0, 1, 2 , 3]) 

    pm_gda_pow_wars = tricity_no2_pollution_data[column_names[6]].to_numpy()
    pm_gda_pow_wars = np.delete(pm_gda_pow_wars, [0, 1, 2 , 3]) 

#model that contains CO polution data as numpy arrays
class TricityCOPoluttionModel:

    #data source parameters 
    file_name = 'data/2021_CO_1g.xlsx'
    column_names = ['Kod stacji', 'PmGdyPorebsk', 'PmSopBiPlowc', 'PmGdaWyzwole', 'PmGdaLeczkow', 'PmGdaPowWars']

    #parse data
    tricity_co_pollution_data = data_parsers.parse_excel_data(file_name, column_names)       

    #define class parameters
    timestamps = tricity_co_pollution_data[column_names[0]].to_numpy()
    timestamps = np.delete(timestamps, [0, 1, 2 , 3]) 

    pm_gdy_porebsk = tricity_co_pollution_data[column_names[1]].to_numpy()
    pm_gdy_porebsk = np.delete(pm_gdy_porebsk, [0, 1, 2 , 3]) 

    pm_sop_bi_plowc = tricity_co_pollution_data[column_names[2]].to_numpy()
    pm_sop_bi_plowc = np.delete(pm_sop_bi_plowc, [0, 1, 2 , 3]) 

    pm_gda_wyzwole = tricity_co_pollution_data[column_names[3]].to_numpy()
    pm_gda_wyzwole = np.delete(pm_gda_wyzwole, [0, 1, 2 , 3]) 
    
    pm_gda_leczkow = tricity_co_pollution_data[column_names[4]].to_numpy()
    pm_gda_leczkow = np.delete(pm_gda_leczkow, [0, 1, 2 , 3]) 

    pm_gda_pow_wars = tricity_co_pollution_data[column_names[5]].to_numpy()
    pm_gda_pow_wars = np.delete(pm_gda_pow_wars, [0, 1, 2 , 3]) 