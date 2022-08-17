import sys
from sklearn.cluster import KMeans
import numpy as np
file = open(sys.argv[1],"r")
line = file.readline()
data = []
eachrow = []


while line != "":
    line = line.replace("\n","")
    eachrow = line.split()
    introw = []
    for e in eachrow:
        e = float(e)
        introw.append(e)
    data.append(introw)
    line = file.readline()

#print(data)

kmeans = KMeans(n_clusters=100, random_state=0, max_iter=300)

kmeans.fit(data)
centers = kmeans.cluster_centers_
labels = kmeans.labels_
np.savetxt("CLL-center.txt",centers)
np.savetxt("CLL-label.txt",labels)


