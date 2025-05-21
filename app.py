import streamlit as st  
import numpy as np
import matplotlib.pyplot as plt  
from algorithm import k_means

st.title("K-Means Clustering Visualization")

data_option = st.selectbox("veri kaynağını seçin", options=["rastgele veri oluştur", "veri yükle"])
if data_option == "rastgele veri oluştur":

    num_points = st.slider("Veri noktası sayısı (Number of data points)", min_value=50, max_value=500, value=200)
    data = np.random.rand(num_points, 2)
else:
    uploaded_file = st.file_uploader("CSV dosyası yükleyin", type="csv")
    if uploaded_file is not None:
        import pandas as pd  
        df = pd.read_csv(uploaded_file)
        data = df.values
    else:
        data = np.array([])

if data.size > 0:
    k = st.slider("küme sayısı", min_value=1, max_value=10, value=3)

    if st.button("algoritmayı çalıştır"):
        clusters, centroids = k_means(data, k)
        

        fig, ax = plt.subplots()
        scatter = ax.scatter(data[:, 0], data[:, 1], c=clusters, cmap="viridis")
        ax.scatter(centroids[:, 0], centroids[:, 1], color="red", marker="X", s=100)
        st.pyplot(fig)
else:
    st.info("lütfen veri oluşturun ya da yükleyin.")

