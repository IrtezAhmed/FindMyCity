import streamlit as st
import pandas as pd
import plotly.express as px

st.write("**Take Me Home, Country Roads**")

st.write("John Denver's words **impacted millions**. Now it's time for it to impact you - where is your home, country roads?")

st.write("With our app, you can find just that.")

#reading all CSV files
cities = pd.read_csv('cities.csv').set_index('City')
CoL = pd.read_csv('movehubcostofliving.csv').set_index('City')
QoL = pd.read_csv('movehubqualityoflife.csv').set_index('City')

result = QoL.join(cities).join(CoL)

st.write(result)

fig = px.scatter_mapbox(result, lat="lat", lon="lng", hover_name="Country", hover_data=["Gasoline", "Cinema"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
                        
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)