# Computational identififcation of CLL and B-ALL leukemic cells for blood cancer diagnosis
## Introduction
Leukemia is a major type of blood cancer. The current diagnosis of leukemia based on flow cytometry data requires a manual data analytical process called manual gating analysis, which is ad hoc, subjective, and labor-intensive. Computational analysis of such high-dimensional single cell data is challenging. Data clustering methods such as K-means provides data-driven insights into phenotypic heterogneity of the cancer cells, which identify cell populations based on examining on celluar expressions of all markers simultaneously. In this project, we assessed multiple computational methods in their ability of identifying blood cancer cells for both sample-level diagnosis and cell-level estimation of cancer burden, using two independent datasets (CLL: chronic lymphocytic leukemia and B-ALL: B-cell lymphoblastic leukemia). 
## Data
### CLL
To reduce the runtime, 10 CLL samples (5 CLL+ and 5 CLL-) were radomly selected to create a template of cluster centriods, using 'kmeans_CLL.py'. The template is stored in 'CLL-center.txt' file. Then this template was used to initalize the K-means clustering process. 87 CLL samples were analyzed for identifying cancer burden and sample-level diagnosis. Without assuming the data to follow a Gaussian distribution, a nonparametric statistical test, Wilcoxon Rank Sum Test, was applied to identify significant cancer cell clusters using "pipeline_with_FDR_correction.ipynb" and "pipeline_without_FDR_correction.ipynb.ipynb", depending on whether a p-value adjustment is necessary for multiple-test correction.

### B-ALL
To reduce the runtime, 3 B-ALL samples with a cancer burden of around 90% were used to generate the Kmeans centriods "template" using 'kmeans.py' and stored in 'BALL-large-center.txt' file. 178 ALL samples were analyzed for identifying the B-ALL cancer burden and the sample-level diagnosis. Besides using the Wilcoxon Rank Sum Test to identify general/global cancer cell clusters, an Emperical Rule was used to identify patient-specific cancer cells, as implemented in "Patient Specific Pipeline-Rank sum test.ipynb".

## Acknowledgement
The work is done as a senior design class project of UCSD Bioengineering, mentored by Dr. Yu “Max” Qian at the J. Craig Venter Institute. The Senior Design class is led by Dr. Bruce Wheeler and our TA Sicily Rose Panattil. The datasets used in the project are de-identified and provided by Dr. Jack Bui of UCSD (CLL) and Dr. Jean Oak of Stanford (B-ALL), following standard diagnostic protocols at UCSD and Stanford. All the FCS files are preprocessed and fully de-identified before being transferred or used in the project.
