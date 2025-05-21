import numpy as np  # NumPy: dizilerle ve matris hesaplamalarıyla çalışmak için

def initialize_centroids(data, k):
    """
    Verilen veri (data) kümesinden rastgele k adet merkez (centroids - merkezler) seçilir.
    """
    indices = np.random.choice(len(data), k, replace=False)
    return data[indices]

def assign_clusters(data, centroids):
    """
    Her veri noktasını (data point - veri noktası) en yakın merkeze (centroid) atar.
    """
    clusters = []
    for point in data:
        distances = np.linalg.norm(point - centroids, axis=1)  # Öklidyen mesafe hesaplaması
        cluster_index = np.argmin(distances)
        clusters.append(cluster_index)
    return np.array(clusters)

def update_centroids(data, clusters, k):
    """
    Her küme (cluster - küme) için yeni merkez değeri (centroid) hesaplanır.
    """
    centroids = []
    for i in range(k):
        points_in_cluster = data[clusters == i]
        if len(points_in_cluster) > 0:
            centroid = np.mean(points_in_cluster, axis=0)
        else:
            centroid = np.zeros(data.shape[1])
        centroids.append(centroid)
    return np.array(centroids)

def k_means(data, k, iterations=100):
    centroids = initialize_centroids(data, k)
    for i in range(iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, clusters, k)
        # Eğer merkezler (centroids) değişmiyorsa, algoritmayı sonlandırır.
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids

