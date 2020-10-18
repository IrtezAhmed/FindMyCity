#clustering aglorithm

from sklearn import cluster
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import math

#calculate distance from home to POI
#distance = math.sqrt(((lat2 - lat1)111)**2 + ((lon2 - lon1)111)**2)

#sample data
randomInput = np.random.rand(1000,5)
randomInput = pd.DataFrame(randomInput, columns=['Pumpkin', 'Tom', 'Grass', 'Jelly', 'Potato'], index = range(1000))

st.write(randomInput)

model = KMeans(n_clusters = 8, n_init=100, init='random')
model.fit(randomInput)

labels = model.predict(randomInput)

#generating random row names
indexNames = []
for i in range(1000):
    indexNames.append('CityName'+str(i))

clusterVal = pd.DataFrame(labels, columns=['Cluster'], index = indexNames)

#creates dictionary values that are easily accessible
clusterDict = {}
n = 0
for clusterNum in labels:
    clusterNum = str(clusterNum)
    if clusterNum in clusterDict:
        clusterDict[clusterNum].append(indexNames[n])
    else:
        clusterDict[clusterNum] = [indexNames[n]]
    n+=1

#printing the dictionary out
'''for clusterNum in clusterDict:
    st.write("Cluster Number:", clusterNum)
    for city in clusterDict[clusterNum]:
        st.write(city)'''

#receiving input from user
userLabel = 

