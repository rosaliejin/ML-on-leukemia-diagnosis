# Kmeans clustering in Assisting ALL and CLL Leukemia Diagnosis
## Introduction
Leukemia is one of the major types of cancer in the United States. The current diagnosis of leukemia based on flow cytometry data through a process called manual gating, can be very subjective, time-consuming, and labor-intensive. Manipulation of such high-dimensional data could be challenging. However, k-means clustering provides great insight into cancer cell identification by clustering the cells based on their markers in different dimensions. In this project, we will assess different computational methods in their ability in identifying blood cancer cells.This project aims to use Kmeans Clustering to provide sample level diagnosis and tumor burden estimation of CLL and ALL leukemia. 
## Data
### CLL
10 CLL dataset are used to generate the Kmeans centriods "template" to reduce the runtime of future analysis. The data used for kmeans centroid generation can be found in the folder 'template' and the script used can be in 'kmeans_CLL.py'. 'CLL_data_analysis.ipynb' is used to provide diagnosis and tumor burden estimation

### ALL
8 CLL dataset are used to generate the Kmeans centriods "template" to reduce the runtime of future analysis. The data used for kmeans centroid generation can be found in the folder 'template' and the script used can be in 'kmeans_ALL.py'. 'ALL_data_analysis.ipynb' is used to provide diagnosis and tumor burden estimation

## Acaknowlegement
The work is done as a senior design class project of UCSD Bioengineering, mentored by Dr. Yu “Max” Qian at the J. Craig Venter Institute. The Senior Design class is led by Dr. Bruce Wheeler and our TA Sicily Rose Panattil. The datasets used in the project are provided by Dr. Jack Bui of UCSD (CLL) and Dr. Jean Oak of Stanford (B-ALL). All the FCS files are preprocessed and fully de-identified before being transferred or used in the project.
