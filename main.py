import streamlit as st
import pandas as pd
import plotly.express as px
import math

st.title("Find My City")
#st.write("**Take Me Home, Country Roads**")

#st.write("John Denver's words **impacted millions**. Now it's time for it to impact you - where is your home, country roads?")

#st.write("With our app, you can find just that.")

#reading all CSV files
# citiesRef = pd.read_csv('cities.csv')
# cities = pd.read_csv('cities.csv').set_index('City')
# CoL = pd.read_csv('movehubcostofliving.csv').set_index('City')
# QoL = pd.read_csv('movehubqualityoflife.csv').set_index('City')
prices = pd.read_csv('prices.csv')
tempCSV = pd.read_csv('tempByState.csv')
statesCSV = pd.read_csv('states.csv')
citiesCSV = pd.read_csv('uscities.csv')
rateCSV = pd.read_csv('unemployment_rate.csv')

citiesCSV = citiesCSV.join(tempCSV.set_index('Location'), on='state_name')
citiesCSV['location'] = citiesCSV['city'] + citiesCSV['county_name']
prices['location'] = prices['City'] + prices['County']

result = citiesCSV.join(prices.set_index('location'), on='location')
result = result.dropna().set_index('city')
result = result[['state_id', 'state_name', 'county_name', 'lat', 'lng', 'population', 'density', 'Value', 'Average Rental Cost']]

result = result.join(rateCSV.set_index('State'), on='state_name')
result['Temp'] = result['Value']
result['Unemployment Rate'] = result['Rate']
result = result.drop(columns=['Rank', 'Value', 'Rate'])

st.write(result)

rows = list(result.index)

userLocation = st.selectbox("Where do you live right now?", rows)
#st.write(userLocation)
userDistance = st.slider("How far are you willing to move away?", 0, 10000, 0, 200)
userPop = st.slider("How populated do you want this city to be? (1 = Sparse, 5 = Crowded)", 1, 5, 1)
userRent = st.slider("How much rent are you willing to pay? (Specify a range)", 600, 22000, (3000, 6000), 100)
userJob = st.slider("How important is the local job market for you? (1 = Not important, 5 = Very important", 1, 5, 1)
userClimate = st.slider("What kind of climate do you prefer? (1 = Cold, 5 = Hot)", 1, 5, 1)

# math.sqrt(((lat2 - lat1)*111)**2 + ((lon2 - lon1)*111)**2)
# st.write(math.sqrt(((result["lat"][1] - result["lat"][2])*111)**2 + ((result["lng"][1] - result["lng"][2])*111)**2))
#May need to multiply final answer by a certain amount
fig = px.scatter_mapbox(result, lat="lat", lon="lng", color="population", hover_name=rows, hover_data=['Average Rental Cost',"Temp"], size="density", 
                        color_continuous_scale=px.colors.diverging.RdYlGn, zoom=1, mapbox_style="carto-positron", size_max=15)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)