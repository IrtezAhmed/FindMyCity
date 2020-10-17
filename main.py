import streamlit as st
import pandas as pd
import plotly.express as px

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
st.write("TEST")

df = px.data.carshare()
fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")
st.plotly_chart(fig)
