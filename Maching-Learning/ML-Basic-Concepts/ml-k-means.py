import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# K-means is an unsupervised learning method for clustering data points.
# The algorithm iteratively divides data points into K clusters by minimizing the variance in each cluster.

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.scatter(x, y)
plt.show()

data = list(zip(x, y))
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

# The "elbow" on the graph above (where the interia becomes more linear) is at K=2
plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# The fitting of K-means algorithm one more time and plot the different clusters assigned to the data
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()