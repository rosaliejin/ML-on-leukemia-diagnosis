# Kmeans clustering in Assisting ALL and CLL Leukemia Diagnosis
## Introduction
Leukemia is one of the major types of cancer in the United States. The current diagnosis of leukemia based on flow cytometry data through a process called manual gating, can be very subjective, time-consuming, and labor-intensive. Manipulation of such high-dimensional data could be challenging. However, k-means clustering provides great insight into cancer cell identification by clustering the cells based on their markers in different dimensions. In this project, we will assess different computational methods in their ability in identifying blood cancer cells.This project aims to use Kmeans Clustering to provide sample level diagnosis and tumor burden estimation of CLL and ALL leukemia. 
## Data
### CLL
10 CLL samples (5 CLL+ and 5 CLL-) are used to generate the Kmeans centriods "template" using 'kmeans_CLL.py' and stored in 'CLL-center.txt' file. The following analysis use this template centroid as initial centroid position to reduce the runtime. In the next step, 87 CLL samples are analyzed for tumor burden and sample level diagnosis using Rank Sum Test to identify significant cancer cluster with and without p value adjustment using "pipeline_with_FDR_correction.ipynb" and "pipeline_without_FDR_correction.ipynb.ipynb" file.

### ALL
3 ALL samples with a tumor burden of around 90% are used to generate the Kmeans centriods "template" using 'kmeans.py' and stored in 'BALL-large-center.txt' file. The following analysis use this template centroid as initial centroid position to reduce the runtime. In the next step, 178 ALL samples are analyzed for tumor burden and sample level diagnosis using Rank Sum Test to identify general cancer cluster and Emperical Rule to identify patient specific clusters in "Patient Specific Pipeline-Rank sum test.ipynb" file.

## Acaknowlegement
The work is done as a senior design class project of UCSD Bioengineering, mentored by Dr. Yu “Max” Qian at the J. Craig Venter Institute. The Senior Design class is led by Dr. Bruce Wheeler and our TA Sicily Rose Panattil. The datasets used in the project are provided by Dr. Jack Bui of UCSD (CLL) and Dr. Jean Oak of Stanford (B-ALL). All the FCS files are preprocessed and fully de-identified before being transferred or used in the project.
