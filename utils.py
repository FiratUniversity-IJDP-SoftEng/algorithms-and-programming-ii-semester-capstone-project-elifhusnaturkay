import matplotlib.pyplot as plt
import numpy as np

def plot_clusters(data, clusters, centroids):
    fig, ax = plt.subplots()
    scatter = ax.scatter(data[:, 0], data[:, 1], c=clusters, cmap="viridis")
    ax.scatter(centroids[:, 0], centroids[:, 1], color="red", marker="X", s=100)
    return fig

