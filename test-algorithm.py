import numpy as np
from algorithm import initialize_centroids, assign_clusters, update_centroids, k_means

def test_initialize_centroids():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    centroids = initialize_centroids(data, 2)
    assert centroids.shape == (2, 2)

def test_assign_clusters():
    data = np.array([[1, 2], [3, 4]])
    centroids = np.array([[1, 2], [3, 4]])
    clusters = assign_clusters(data, centroids)
    assert (clusters == np.array([0, 1])).all()

def test_k_means():
    data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    clusters, centroids = k_means(data, 2, iterations=10)
    assert len(centroids) == 2

if __name__ == "__main__":
    test_initialize_centroids()
    test_assign_clusters()
    test_k_means()
    print("Tüm testler başarılı!")

