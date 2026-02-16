import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Hierarchical clustering is an unsupervised learning method for clustering data points.
# The algorithm builds data using dissimilarities between data points. Reference: https://www.w3schools.com/python/python_ml_hierarchial_clustering.asp

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# data to set of points
data = list(zip(x, y))

# computing linkage between all points with euclidean distance measure and ward's linkage which seeks to minimize the variance between clusters
linkage_data = linkage(data, method='ward', metric='euclidean')
# plotting result with dendrogram
dendrogram(linkage_data)
plt.show()

# with AgglomerativeClustering with 2 clusters and ward linkage, allows us to use hierarchical clustering in different manner
hierarchical_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
# computing clusters for defined data points
labels = hierarchical_cluster.fit_predict(data)
# plotting cluster
plt.scatter(x, y, c=labels)
plt.show()