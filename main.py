import streamlit as st
import pandas as pd
import plotly.express as px

st.write("**Take Me Home, Country Roads**")

st.write("John Denver's words **impacted millions**. Now it's time for it to impact you - where is your home, country roads?")

st.write("With our app, you can find just that.")

#reading all CSV files
citiesRef = pd.read_csv('cities.csv')
cities = pd.read_csv('cities.csv').set_index('City')
CoL = pd.read_csv('movehubcostofliving.csv').set_index('City')
QoL = pd.read_csv('movehubqualityoflife.csv').set_index('City')

result = cities.join(QoL).join(CoL)

result = result.dropna()

st.write(result)

rows = list(result.index)

fig = px.scatter_mapbox(result, lat="lat", lon="lng", color="Movehub Rating", hover_name=rows, size="Quality of Life", 
                        color_continuous_scale=px.colors.diverging.RdYlGn, zoom=1, mapbox_style="carto-positron", size_max=15)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)