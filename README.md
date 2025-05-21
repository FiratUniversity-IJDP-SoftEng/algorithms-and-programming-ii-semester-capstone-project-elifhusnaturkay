# K-Means Algorithm - Interactive Visualization

## Project Overview

This project is an interactive web application that implements and visualizes the **K-Means Clustering Algorithm**, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

The K-Means algorithm is an unsupervised learning technique used for clustering data points into a predefined number of clusters (k). It works by minimizing the within-cluster sum of squares (inertia) and is widely used in data mining, computer vision, and pattern recognition tasks.

### Problem Definition

The problem is to group a given dataset into **k clusters** such that data points within the same cluster are as similar as possible, while points from different clusters are as dissimilar as possible. It is particularly useful when the structure or labeling of data is unknown.

### Mathematical Background

The K-Means algorithm aims to minimize the following **objective function**:

$$
J = \sum_{i=1}^{k} \sum_{x \in C_i} \| x - \mu_i \|^2
$$

Where:

* $k$: Number of clusters
* $C_i$: Set of points in cluster i
* $\mu_i$: Centroid of cluster i
* $\| x - \mu_i \|^2$: Squared Euclidean distance between a point and its cluster centroid

### Algorithm Steps

1. **Initialize** k centroids randomly.
2. **Assign** each data point to the closest centroid.
3. **Update** centroids by calculating the mean of all points assigned to that cluster.
4. **Repeat** steps 2–3 until centroids no longer move significantly or a maximum number of iterations is reached.

### Pseudocode

```
Initialize k centroids randomly
repeat
    Assign each point to the nearest centroid
    Update centroids as the mean of the assigned points
until centroids converge or max_iterations reached
```

## Complexity Analysis

### Time Complexity

* **Best Case:** O(nkt) - When convergence is quick
* **Average Case:** O(nkt) - n: number of data points, k: number of clusters, t: iterations
* **Worst Case:** O(nkt) - In case of slow convergence

### Space Complexity

* O(n + k) - For storing data points and centroids

## Features

* Interactive visualization of K-Means clustering
* Dynamic cluster number adjustment
* Real-time centroid updates
* Visual feedback for each clustering iteration

## Screenshots

![Main Interface](/Users/elifhusnaturkay/github-classroom/FiratUniversity-IJDP-SoftEng/algorithms-and-programming-ii-semester-capstone-project-elifhusnaturkay/k_means_streamlit.png)

## Usage Guide

1. Select or upload a dataset
2. Choose the desired number of clusters (k)
3. Click 'Run Algorithm' to initiate clustering
4. Observe the visualization of cluster assignments and centroid movements

### Example Inputs

* Dataset with 2D coordinates and k = 3 → clusters the data into 3 groups
* Dataset with non-linearly separable data → demonstrates K-Means limitations

## Testing

### Test Cases

* Dataset with obvious cluster separation (expected: correct assignment)
* Dataset with overlapping clusters (expected: reasonable separation)
* Dataset with noise/outliers (expected: core clustering remains accurate)

## Limitations and Future Improvements

### Current Limitations

* Does not handle non-convex clusters well
* Sensitive to initial centroid selection
* Requires specifying k manually

### Planned Improvements

* Implement k-means++ initialization
* Integrate elbow method to suggest optimal k
* Extend to support multi-dimensional data and more advanced distance metrics

## References and Resources

### Academic References

1. MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations.
2. Jain, A. K. (2010). Data clustering: 50 years beyond K-means.
3. Lloyd, S. P. (1982). Least squares quantization in PCM.

### Online Resources

* [https://scikit-learn.org/stable/modules/clustering.html#k-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
* [https://en.wikipedia.org/wiki/K-means\_clustering](https://en.wikipedia.org/wiki/K-means_clustering)
* [https://www.geeksforgeeks.org/ml-k-means-algorithm/](https://www.geeksforgeeks.org/ml-k-means-algorithm/)

## Author

* **Name:** \[Elif Hüsna Turkay]
* **Student ID:** \[220543003]
* **GitHub:** \[elifhusnaturkay]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project, and the course instructors who contributed to the foundation of this project.

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
