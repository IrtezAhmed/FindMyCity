from sklearn import cluster
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import math
import plotly.express as px
import pickle

st.title("Find My City")
st.write("**'Take Me Home, Country Roads'**")
st.write("John Denver's words **impacted millions**. Now it's time for it to impact you - where is your home, country roads?")
st.write("With our app, you can find just that.")

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

#results isolated to relevant information
resultFinal = result[['density', 'Average Rental Cost', 'Temp', 'Unemployment Rate']]


st.write(resultFinal) #final result

rows = list(resultFinal.index)

userLocation = st.selectbox("Where do you live right now?", rows)

userLat = result.loc[userLocation]['lat']
userLng = result.loc[userLocation]['lng']

userDistance = st.slider("How far are you willing to move away?", 0, 10000, 0, 200)

userPop = st.slider("How populated do you want this city to be? (1 = Sparse, 5 = Crowded)", 1, 5, 1)*6600
userRent = st.slider("How much rent are you willing to pay? (Specify a range)", 600, 22000, (3000, 6000), 100)
userRentMedian =  int((userRent[0] +  userRent[1])/2)
userJob = st.slider("How important is the local job market for you? (1 = Not important, 5 = Very important", 1, 5, 1)*200
userClimate = st.slider("What kind of climate do you prefer? (1 = Cold, 5 = Hot)", 1, 5, 1)
actualClimate = int(userClimate*600)+40

#clustering algorithm
st.write('TRAINING......')
model = KMeans(n_clusters = 100, n_init=100, init='random')
model.fit(resultFinal)
labels = model.predict(resultFinal)
pickle.dump(model, open('mode.sav', 'wb'))
st.write("TRAINING COMPLETE.")

np.save('label.npy', labels)
st.write('TRAINING COMPLETE')
clusterVal = pd.DataFrame(labels, columns=['Cluster'], index = rows) #creates a DF of cities to their respective clusters

#creates dictionary values that are easily accessible
clusterDict = {}
n = 0
for clusterNum in labels:
    clusterNum = str(clusterNum)
    if clusterNum in clusterDict:
        clusterDict[clusterNum].append(rows[n])
    else:
        clusterDict[clusterNum] = [rows[n]]
    n+=1

np.save('dictionary.npy', clusterDict)

loadModel = pickle.load(open('mode.sav', 'rb'))
read_labels = np.load('label.npy',allow_pickle='TRUE')
read_dictionary = np.load('dictionary.npy',allow_pickle='TRUE').item()

#receiving input from user
userValues = {"density": userPop, "Average Rental Cost":userRentMedian, "Temp":actualClimate, "Unemployment Rate":userJob}
userDF = pd.DataFrame(data=userValues, index = ['User'])
st.write(userDF)
userLabel = loadModel.predict(userDF)

#st.write(userLabel)

#return list of cities within relevant cluster

clusterDict = read_dictionary

st.write('**Here are the top 3 cities recommended for you!**')

#printing the dictionary out
count = 0
while len(clusterDict[str(userLabel[0])])>3 and count<3:
    for city in clusterDict[str(userLabel[0])]:
        if count <3:
            st.write(city)
            count+=1
        else:
            break

#color all cities within the same cluster as green, and all the other clusters closer to red

finalLabel = pd.DataFrame(read_labels, columns=['Cluster'], index = rows) #creates a DF of cities to their respective clusters
#resultFinal = resultFinal.join(finalLabel)

#end clustering algorithm

# math.sqrt(((lat2 - lat1)*111)**2 + ((lon2 - lon1)*111)**2)
# st.write(math.sqrt(((result["lat"][1] - result["lat"][2])*111)**2 + ((result["lng"][1] - result["lng"][2])*111)**2))
#May need to multiply final answer by a certain amount
fig = px.scatter_mapbox(result, lat="lat", lon="lng", color="population", hover_name=rows, hover_data=['Average Rental Cost',"Temp"], size="density", 
                        color_continuous_scale=px.colors.diverging.RdYlGn, zoom=1, mapbox_style="carto-positron", size_max=15)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)