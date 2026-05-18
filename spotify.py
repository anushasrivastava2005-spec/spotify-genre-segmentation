import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

df = pd.read_csv("spotify dataset.csv")

num_features = [
    'track_popularity',
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'duration_ms'
]

# Distribution plots
plt.figure(figsize=(8, 10))

for i, feature in enumerate(num_features):
    plt.subplot(4, 3, i + 1)
    sns.histplot(df[feature], kde=True, color='skyblue')
    plt.title(f'Distribution of {feature}')

plt.tight_layout()
plt.show()

# Playlist genre count plot
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x='playlist_genre',
    order=df['playlist_genre'].value_counts().index
)

plt.title("Playlist Genre Counts")
plt.xticks(rotation=45)
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))

corr = df[num_features].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')

plt.title("Feature Correlation Matrix")
plt.show()

# Feature scaling
X = df[num_features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Finding optimal number of clusters using silhouette score
scores = []

for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)
    scores.append(score)

# Plot silhouette scores
plt.plot(range(2, 10), scores, marker='o')

plt.title("Silhouette Score vs Number of Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")

plt.show()

# Assume best k = 4
kmeans = KMeans(n_clusters=4, random_state=42)

df['cluster'] = kmeans.fit_predict(X_scaled)

# Reduce dimensions for visualization
pca = PCA(n_components=2)

components = pca.fit_transform(X_scaled)

df['pca1'] = components[:, 0]
df['pca2'] = components[:, 1]

# Plot PCA clusters
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='pca1',
    y='pca2',
    hue='cluster',
    palette='Set2'
)

plt.title("Cluster Visualization using PCA")
plt.show()
