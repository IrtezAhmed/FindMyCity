'''#clustering algorithm
st.write('TRAINING......')
model = KMeans(n_clusters = 100, n_init=100, init='random')
model.fit(resultFinal)
#labels = model.predict(resultFinal)
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

np.save('dictionary.npy', clusterDict)'''




