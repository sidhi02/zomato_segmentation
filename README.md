# 🍽️ Restaurant Clustering & Segmentation using Machine Learning

<p align="center">
<img src="images/banner.png" width="100%">
</p>

## 📖 Project Overview

Restaurant businesses generate large amounts of operational and customer-related data every day. Understanding this data is essential for identifying customer preferences, pricing trends, and restaurant characteristics. However, manually analyzing thousands of restaurants can be challenging.

This project applies **Unsupervised Machine Learning** techniques to segment restaurants into meaningful clusters based on various attributes such as pricing, ratings, cuisines, and customer engagement. Three clustering algorithms—**K-Means**, **Agglomerative Clustering**, and **DBSCAN**—were implemented and compared to discover hidden patterns within the dataset.

The resulting clusters provide valuable business insights that can support pricing strategies, customer targeting, market expansion, and restaurant recommendation systems.

---

# ❓ Problem Statement

Restaurants differ significantly in terms of pricing, cuisines, ratings, and customer popularity. Businesses often struggle to identify groups of similar restaurants without predefined labels.

The objective of this project is to use clustering techniques to automatically segment restaurants into meaningful groups, allowing businesses to better understand the market and make data-driven decisions.

---

# 🎯 Objectives

- Clean and preprocess the restaurant dataset.
- Perform Exploratory Data Analysis (EDA).
- Identify important restaurant characteristics.
- Scale numerical features for clustering.
- Apply multiple clustering algorithms.
- Compare clustering models.
- Interpret restaurant segments.
- Generate meaningful business insights.

---

# 📂 Dataset Description

The project uses the **Zomato Restaurant Dataset**, which contains information about restaurants such as:

- Restaurant Name
- Location
- Average Cost for Two
- Online Order Availability
- Table Booking
- Restaurant Type
- Cuisines
- Average Rating
- Number of Votes

These features were used to analyze restaurant behavior and perform clustering.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- StandardScaler
- PCA
- K-Means Clustering
- Agglomerative Clustering
- DBSCAN

---

# ⚙️ Project Workflow

```text
Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Feature Engineering
    │
    ▼
Feature Scaling
    │
    ▼
Clustering Algorithms
    │
    ├── K-Means
    ├── Agglomerative
    └── DBSCAN
    │
    ▼
Model Comparison
    │
    ▼
Business Insights
```

---

# 📊 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand pricing patterns, customer ratings, cuisine popularity, and restaurant characteristics before applying clustering algorithms.

---

# 💰 1. Restaurant Cost Distribution

<p align="center">
<![Cost Distribution](zomato/images/cost_distribution.png)>
</p>

### 📖 Observation

- The majority of restaurants have an average cost between **₹400 and ₹1000** for two people.
- Premium restaurants charging more than **₹2000** are comparatively fewer.
- The distribution is positively skewed, indicating that expensive restaurants are relatively uncommon.

### 💼 Business Insight

The restaurant market is primarily dominated by **budget and mid-range restaurants**. Businesses entering the market may benefit from focusing on affordable pricing strategies, as they cater to the largest customer segment.

---

# ⭐ 2. Average Cost vs Average Rating

<p align="center">
  <img src="zomato/images/cost_distribution.png" width="750">
</p>

### 📖 Observation

- Restaurants with higher prices often receive good ratings.
- However, many affordable restaurants also achieve ratings above **4.0**.
- There is no strong linear relationship between pricing and customer ratings.

### 💼 Business Insight

Higher pricing alone does not guarantee better customer satisfaction. Restaurants should prioritize food quality, service, and overall customer experience rather than relying solely on premium pricing.

---

# 🍜 3. Most Popular Cuisines

<p align="center">
<img src="images/cuisine_popularity.png" width="750">
</p>

### 📖 Observation

- **North Indian cuisine** is the most common cuisine in the dataset.
- Chinese cuisine ranks second in popularity.
- Biryani, Continental, Fast Food, Asian, and Italian cuisines also have a significant presence.

### 💼 Business Insight

North Indian and Chinese cuisines dominate the restaurant market, indicating strong customer demand. Less common cuisines may provide opportunities for niche restaurants to differentiate themselves.

---

# 🍽️ 4. Most Reviewed Restaurants

<p align="center">
<img src="images/most_reviewed_restaurants.png" width="750">
</p>

### 📖 Observation

The selected restaurants exhibit similar review counts in the current visualization, indicating consistent customer engagement among these entries.

> **Note:** If this graph was generated without sorting by review count, it is recommended to regenerate it using the highest review counts for a more accurate representation.

### 💼 Business Insight

Restaurants with higher customer engagement generally have stronger brand visibility and can leverage positive customer interactions to attract more visitors.

---

# ⭐ 5. Rating Distribution

<p align="center">
<img src="images/rating_distribution.png" width="750">
</p>

### 📖 Observation

- Most restaurants have ratings between **4.0 and 5.0**.
- Very few restaurants have ratings below **3.0**.
- The dataset is heavily concentrated around higher customer ratings.

### 💼 Business Insight

Since most restaurants maintain high ratings, additional factors such as pricing, cuisine, and customer engagement become important for differentiating restaurant segments.

---

# 🧹 Data Preprocessing

Before applying clustering algorithms, the dataset was cleaned and transformed to improve data quality and ensure meaningful clustering results.

The preprocessing steps included:

- Removed duplicate records.
- Handled missing values.
- Selected relevant numerical features for clustering.
- Renamed columns for better readability.
- Checked data types and converted them where necessary.
- Removed unnecessary columns that did not contribute to clustering.

Proper preprocessing helps reduce noise and improves the overall quality of the clusters.

---

# ⚖️ Feature Scaling

Since clustering algorithms are distance-based, features with larger numerical values can dominate the clustering process.

To avoid this issue, **StandardScaler** was used to standardize the selected numerical features.

### Why Feature Scaling?

- Prevents features with larger values from dominating.
- Improves clustering accuracy.
- Ensures all features contribute equally.
- Produces more balanced clusters.

---

# 🤖 Clustering Algorithms

Three different clustering algorithms were implemented and compared to identify the most meaningful restaurant segments.

---

## 1️⃣ K-Means Clustering

K-Means is a partition-based clustering algorithm that divides data into **K** distinct clusters by minimizing the distance between data points and their cluster centroids.

### Why K-Means?

- Fast and computationally efficient
- Easy to interpret
- Suitable for large datasets
- Produces well-defined clusters

### Workflow

- Select the number of clusters.
- Initialize cluster centroids.
- Assign each restaurant to the nearest centroid.
- Update centroids.
- Repeat until convergence.

---

## 2️⃣ Agglomerative Clustering

Agglomerative Clustering is a hierarchical clustering technique that starts by treating every restaurant as an individual cluster and gradually merges similar clusters.

### Why Agglomerative Clustering?

- Captures hierarchical relationships
- Does not rely on random initialization
- Useful for understanding cluster structures

### Workflow

- Treat every restaurant as its own cluster.
- Calculate distances between clusters.
- Merge the closest clusters.
- Continue until the desired number of clusters is reached.

---

## 3️⃣ DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups restaurants based on the density of data points instead of predefined cluster centers.

### Why DBSCAN?

- Detects outliers automatically
- Finds clusters of arbitrary shapes
- Does not require specifying the number of clusters

### Workflow

- Identify dense regions.
- Expand clusters from dense points.
- Mark sparse points as outliers.

---

# 📈 Model Comparison

Three clustering algorithms were implemented and evaluated to understand their strengths and suitability for restaurant segmentation.

| Algorithm | Advantages | Limitations |
|------------|------------|-------------|
| K-Means | Fast, simple, interpretable | Requires predefined number of clusters |
| Agglomerative | Reveals hierarchical relationships | Computationally expensive for large datasets |
| DBSCAN | Detects noise and irregular clusters | Sensitive to parameter selection |

Among these methods, **K-Means** produced the most interpretable and well-separated clusters for this dataset, making it the preferred choice for segmenting restaurants.

---

# 🎯 Cluster Interpretation

The clustering process grouped restaurants with similar characteristics into distinct segments.

The identified clusters generally represented:

- 💰 Budget-friendly restaurants
- 🍴 Mid-range restaurants
- ⭐ Highly rated restaurants
- 💎 Premium restaurants
- 📈 Restaurants with strong customer engagement

These clusters provide valuable insights for market analysis, pricing strategies, and customer targeting.

---

# 💡 Key Business Insights

Based on the exploratory analysis and clustering results, the following insights were identified:

- Most restaurants fall within the budget and mid-range pricing categories.
- Higher prices do not necessarily guarantee better customer ratings.
- North Indian and Chinese cuisines dominate the restaurant market.
- Customer ratings are generally high across the dataset.
- Restaurant segmentation can support targeted marketing campaigns.
- Businesses can use clustering to identify competitors within similar market segments.
- Customer engagement plays an important role in restaurant popularity.

---

# ✅ Conclusion

This project demonstrates how **Unsupervised Machine Learning** can uncover meaningful patterns within restaurant data without requiring predefined labels.

By applying **K-Means**, **Agglomerative Clustering**, and **DBSCAN**, restaurants were successfully grouped into meaningful segments based on pricing, ratings, cuisines, and customer engagement.

These insights can help restaurant owners and businesses make informed decisions related to pricing strategies, customer targeting, expansion planning, and market positioning.

---

# 🚀 Future Scope

This project can be further enhanced by:

- Developing an interactive dashboard using **Power BI** or **Tableau**.
- Deploying the clustering model as a web application using **Flask** or **Streamlit**.
- Incorporating customer review sentiment analysis.
- Building a restaurant recommendation system.
- Applying advanced clustering techniques to improve segmentation.

---

# 📁 Project Structure

```text
Restaurant-Clustering/
│
├── Dataset/
│   └── zomato.csv
│
├── images/
│   ├── banner.png
│   ├── cost_distribution.png
│   ├── cost_vs_rating.png
│   ├── cuisine_popularity.png
│   ├── most_reviewed_restaurants.png
│   └── rating_distribution.png
│
├── zomato_project.ipynb
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 💻 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Restaurant-Clustering.git
```

Navigate to the project directory:

```bash
cd Restaurant-Clustering
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

# ▶️ How to Run

1. Clone this repository.
2. Install the required dependencies.
3. Open `zomato_project.ipynb`.
4. Run the notebook sequentially.
5. Explore the visualizations, clustering results, and business insights.

---

# 📦 Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🙌 Acknowledgements

- Zomato Restaurant Dataset
- Scikit-learn Documentation
- Pandas Documentation
- Matplotlib Documentation

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
