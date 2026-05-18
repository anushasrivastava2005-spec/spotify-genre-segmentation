Spotify’s recommendation system works by analyzing similarities between songs based on their audio characteristics.
In this project, we perform:

Data Preprocessing
Exploratory Data Analysis (EDA)
Correlation Analysis
Clustering using K-Means
PCA-based Cluster Visualization
Genre-based Segmentation

The goal is to group similar songs together so that a recommendation system can later suggest songs with related musical patterns.

🚀 Features

✔️ Data Cleaning & Preprocessing
✔️ Audio Feature Analysis
✔️ Correlation Heatmap
✔️ Genre Distribution Visualization
✔️ K-Means Clustering
✔️ Silhouette Score Evaluation
✔️ PCA Dimensionality Reduction
✔️ Cluster Visualization

🛠️ Technologies Used
Python
Pandas
Matplotlib
Seaborn
Scikit-learn
📂 Dataset Features

The dataset contains Spotify song attributes such as:

Track Popularity
Danceability
Energy
Loudness
Speechiness
Acousticness
Instrumentalness
Liveness
Valence
Tempo
Duration

These features are used to identify similarities between songs and create clusters.

📊 Data Analysis & Visualization

The project includes several visualizations:

1️⃣ Feature Distribution Plots

Histogram plots are used to analyze the distribution of different song features.

2️⃣ Playlist Genre Count

A count plot is created to observe the number of songs present in each playlist genre.

3️⃣ Correlation Matrix

A heatmap is used to identify relationships between different audio features.

4️⃣ Silhouette Score Plot

Used to determine the optimal number of clusters for K-Means clustering.

5️⃣ PCA Cluster Visualization

Principal Component Analysis (PCA) reduces dimensions and visualizes clusters in 2D space.

🤖 Machine Learning Model

The clustering model used in this project is:

K-Means Clustering

Steps followed:

Feature Scaling using StandardScaler
Finding optimal clusters using Silhouette Score
Applying K-Means clustering
Visualizing clusters using PCA

The model groups songs with similar audio characteristics together.

📈 Workflow
Dataset Collection
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Scaling
        ↓
K-Means Clustering
        ↓
PCA Visualization
        ↓
Genre Segmentation
▶️ How to Run the Project
1. Clone the Repository
git clone https://github.com/your-username/spotify-genre-segmentation.git
2. Install Dependencies
pip install pandas matplotlib seaborn scikit-learn
3. Run the Python File
python spotify_genre_segmentation.py
📷 Output

The project generates:

Distribution Graphs
Genre Count Charts
Correlation Heatmaps
Silhouette Score Graph
PCA Cluster Scatter Plot

These outputs help in understanding song similarity and genre segmentation.

🎯 Future Improvements
Build a complete music recommendation system
Deploy using Streamlit or Flask
Use Deep Learning for advanced recommendations
Add real-time Spotify API integration
👩‍💻 Author

Anusha Srivastava

📄 License

This project is for educational and learning purposes.
