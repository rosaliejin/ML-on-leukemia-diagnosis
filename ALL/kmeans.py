import sys
from sklearn.cluster import KMeans
import numpy as np
file = open(sys.argv[1],"r")
line = file.readline()
data = []
eachrow = []

#c = open("B-ALL-center.txt", "a")
#l = open("B-ALL-label.txt", "a")

while line != "":
    line = line.replace("\n","")
    eachrow = line.split()
    introw = []
    for e in eachrow:
        e = float(e)
        introw.append(e)
    data.append(introw)
    line = file.readline()

print(data)

kmeans = KMeans(n_clusters=300, random_state=0, max_iter=300)
#kmeans = KMeans(n_clusters=5, random_state=0, max_iter=20)
kmeans.fit(data)
print(centers)
centers = kmeans.cluster_centers_
labels = kmeans.labels_
np.savetxt("BALL-large-300-center.txt",centers)
np.savetxt("BALL-large-300-label.txt",labels)
#print(centers)
#print(labels)
#a = np.array2string(centers,  separator=',')
#b = np.array2string(labels,  separator=',')
#c.write(a)
#l.write(b)
#c.close()
#l.close()
