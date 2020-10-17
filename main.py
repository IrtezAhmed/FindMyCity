

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
result = result.join(qolCSV)
result = result.dropna()
# result = pd.concat([colCSV, citiesCSV], axis=1, join='inner')
st.write(result)

fig = px.scatter_mapbox(result, lat="lat", lon="lng", hover_name="Country", hover_data=["Gasoline", "Cinema"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)
