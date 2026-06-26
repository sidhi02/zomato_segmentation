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
<img src="images/cost_distribution.png" width="750">
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
<img src="images/cost_vs_rating.png" width="750">
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
