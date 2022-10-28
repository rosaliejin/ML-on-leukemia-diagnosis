import numpy as np
np.set_printoptions(suppress=True)
import pandas as pd
from sklearn.cluster import KMeans
from scipy.stats import ranksums
import matplotlib.pyplot as plt
#%matplotlib inline
import random

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)


center = np.loadtxt("CLL-center.txt")

list_to_run = [
"22663",
"29896",
"5807",
"22158",
"15032",
"24046",
"25067",
"26099",
"19252",
"20307",
"24830",
"28047",
"28066",
"28476",
"29593",
"8372",
"9531",
"19328",
"20268",
"25451",
"29842",
"29876",
"5071",
"17988",
"8385",
"8485",
"20121",
"29881",
"30089",
"29860",
"5832",
"6541",
"7420",
"7725",
"13045",
"13088",
"19830",
"19833",
"20706",
"24215",
"25424",
"26129",
"6535",
"19303",
"22936",
"23172",
"30034",
"8604",
"9444",
"9462",
"15030",
"20218",
"24196",
"28856",
"18140",
"18515",
"19494",
"19633",
"24084",
"25664",
"26450",
"28707",
"7495",
"19256",
"15058",
"9422",
"16331",
"20735",
"23184",
"24242",
"24793",
"9343",
"21741",
"24477",
"26207",
"29515",
"5121",
"18736",
"28032",
"14470",
"16327",
"20424",
"7805",
"19363"]

cluster = [6,18,28,44,73,87,25,70,12,15,17,24,56,96]

for a in list_to_run:
    print(a)
    data = pd.read_csv("testing/"+a+".txt.txt",sep = "\t")

    #train kmeans with new data
    data = data.to_numpy()
    kmeans = KMeans(n_clusters=100,init=center, random_state=0, max_iter=2)
    kmeans.fit(data)
    label = kmeans.labels_
    L = label.shape
    
    tumor = []
    healthy = []
    
    for i in range(0,len(label)):
        if label[i] in cluster:
            tumor.append(data[i])
        else:
            healthy.append(data[i])
        
        
    healthy = np.array(healthy)
    tumor = np.array(tumor)
    
    idx = random.sample(range(len(healthy)), int(len(healthy)*0.2))
    healthy = healthy[idx]
    if(len(tumor)>100):
        idx = random.sample(range(len(tumor)), int(len(tumor)*0.2))
    tumor = tumor[idx]
    


    fig, axs = plt.subplots(2,figsize=(3,6))
    fig.suptitle('Cancer cell distribution for sample '+a)



    for x1,y1 in zip(healthy[:,8], healthy[:,9]):
        axs[0].plot(x1,y1,"o",color="blue", alpha=0.7,  markersize = 2)
    
    for x1,y1 in zip(tumor[:,8], tumor[:,9]):
        axs[0].plot(x1,y1,"o",color="red", alpha=0.7,  markersize = 2)    
    axs[0].set(xlabel='CD5', ylabel='CD19' )
    

    for x2,y2 in zip(healthy[:,13], healthy[:,10]):
        axs[1].plot(x2,y2,"o",color="blue", alpha=0.7,  markersize=2)
    
    for x2,y2 in zip(tumor[:,13], tumor[:,10]):
        axs[1].plot(x2,y2,"o",color="red", alpha=0.7,  markersize=2)
    axs[1].set(xlabel='CD10', ylabel='CD79b' )

    plt.savefig(a+".png",bbox_inches="tight")
    #plt.show()
