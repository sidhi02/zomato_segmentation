import pandas as pd
import joblib

model = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

print("=" * 38)
print(" ZOMATO RESTAURANT SEGMENT PREDICTOR ")
print("=" * 38)

cost = float(input("Enter Restaurant Cost: "))
rating = float(input("Enter Average Rating: "))

new_data = pd.DataFrame({
    "Cost": [cost],
    "Avg_Rating": [rating]
})

scaled_data = scaler.transform(new_data)

cluster = model.predict(scaled_data)[0]

cluster_names = {
    0: "Mid-Range Restaurant",
    1: "Premium Restaurant",
    2: "Budget Restaurant"
}

print("\nPredicted Segment:")
print(cluster_names[cluster])

print("\nThank you for using Zomato Restaurant Segment Predictor")