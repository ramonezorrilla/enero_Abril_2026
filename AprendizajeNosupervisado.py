from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X =[[100], [150], [200],[800],[850],[900]]
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print(kmeans.labels_)

plt.scatter(range(len(X)), X, c=kmeans.labels_)
plt.show()
