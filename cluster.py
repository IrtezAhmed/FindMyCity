#clustering aglorithm

from sklearn import cluster
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from main.py import result

model = KMeans(n_clusters = 3, n_init=100, init='random')
model.fit()

print(result)







