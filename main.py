import streamlit as st
import pandas as pd

citiesCSV = pd.read_csv('cities.csv')
colCSV = pd.read_csv('movehubcostofliving.csv')
qolCSV = pd.read_csv('movehubqualityoflife.csv')
priceCSV = pd.read_csv('price.csv')
pricePerSqftCSV = pd.read_csv('pricepersqft.csv')

# dt = colCSV.set_index('City').join(citiesCSV.set_index('City'))

colCSV = colCSV.set_index('City')
citiesCSV = citiesCSV.set_index('City')
result = colCSV.join(citiesCSV)
result = result.dropna()
# result = pd.concat([colCSV, citiesCSV], axis=1, join='inner')
st.write(result)
