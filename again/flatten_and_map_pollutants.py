from scipy import interpolate
import json
import pandas as pd
import csv
import time

pollutantList = ['CO2', 'CO', 'NOX', 'VOC', 'SO2', 'NH3', 'PM10', 'PM2.5']

#record data to interpolate
pollutantFile = open('record_results_final.csv', mode='r')
pollutantReader = csv.DictReader(pollutantFile)
interpolationData = {'Speed': [i for i in range(0, 81)], 'CO':[], 'NOX':[], 'VOC':[], 'SO2':[], 'NH3':[], 'PM10':[], 'PM2.5':[]}
for row in pollutantReader:
    for pollutant in pollutantList:
        interpolationData[pollutant].append(row[pollutant])

#create interpolation functions for each pollutant
interpolationFunctions = {}
for pollutant in pollutantList:
    interpolationFunctions[pollutant] = interpolate.interp1d(interpolationData['Speed'], interpolationData[pollutant])


outputFile = open('flattened_with_emissions.csv', mode='a')

#now, retrieve dataframes - this reads in one chunk??? /figure out how exactly the data is structured...
df = pd.read_csv('test.csv')
df = df.drop_duplicates(['uuid'])
for pollutant in pollutantList: #scale pollutant based on speed by the length
        # scale by volume of cars (find # of cars that can fit on the road, and divide that by how long it takes to get through the road to get # of cars/hr)
    df[pollutant] = (interpolationFunctions[pollutant](df['speed']))*(df['length']/1.60934)*((df['length']/6)*3)*(1/(df['length']*1000/df['speed']))
df.to_csv(outputFile, header=False)
