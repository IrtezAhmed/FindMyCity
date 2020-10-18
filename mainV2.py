import streamlit as st
import pandas as pd

citiesCSV = pd.read_csv('cities.csv')
colCSV = pd.read_csv('movehubcostofliving.csv')
qolCSV = pd.read_csv('movehubqualityoflife.csv')
priceCSV = pd.read_csv('price.csv')
pricePerSqftCSV = pd.read_csv('pricepersqft.csv')

tempCSV = pd.read_csv('tempByCity.csv')
for i in range(0,len(tempCSV)):
    index = tempCSV.iloc[i, 1].find(', ')
    tempCSV.iloc[i, 1] = tempCSV.iloc[i, 1][:index]
tempCSV = tempCSV.set_index('Location')
tempCSV = tempCSV['Value']

colCSV = colCSV.set_index('City')
citiesCSV = citiesCSV.set_index('City')
result = colCSV.join(citiesCSV).join(tempCSV)
result = result.dropna()
# result = pd.concat([colCSV, citiesCSV], axis=1, join='inner')
st.write(result)
